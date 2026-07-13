## ============ Librerias ============
# Principales
from machine import Pin
import network
import socket
import time
# Status
import os # Memoria Flash
import gc # Garbage Collector (Memoria Ram)
import json # Enviar al navegador info de manera facil
import machine # Estado CPU
# Comunicacion Externa
from umqtt.simple import MQTTClient

## ============ WI-FI ============
ssid = "Speedy-Fibra-83113E"
password = "88598HC8CK672f57F545"
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print("Conectando...")

timeout = 15

while not wlan.isconnected() and timeout > 0:
    print(".", end="")
    time.sleep(1)
    timeout-=1

if wlan.isconnected():
    print("Conectado a:", ssid)
    print("IP:", wlan.ifconfig()[0])
else:
    print("\nNo se pudo conectar")


## ============ Dispositivos Locales ============
pin_pulsos = Pin(0, Pin.OUT) # Clock
pin_binario = Pin(2, Pin.OUT) # Data
pin_subir = Pin(15, Pin.OUT) # Latch

def shift_out(data_pin, clock_pin, value):
    # MSBFIRST (El bit más significativo primero)
    for i in range(7, -1, -1):
        # Ponemos el bit en el pin de datos
        data_pin.value((value >> i) & 1)
        
        # Generamos el pulso de reloj
        clock_pin.value(1)
        clock_pin.value(0)

def num_display(num):
    tabla = {
        0: 0x7F, 1: 0x0C, 2: 0xB6, 3: 0x9F, 4: 0xCC,
        5: 0xDB, 6: 0xFA, 7: 0x0F, 8: 0xFF, 9: 0xCF
    }
    return tabla.get(num, 0x00)

def poner_num_7_display(num):
    pin_subir.value(0)
    shift_out(pin_binario, pin_pulsos, num_display(num))
    pin_subir.value(1) 
    
ips_conectadas = set()
historical_connected_devices = 0
def registrar_acceso(ip_cliente):
    global historical_connected_devices
    ips_conectadas.add(ip_cliente)
    print(f"IP registrada: {ip_cliente}")
    print(f"Total de dispositivos únicos: ", len(ips_conectadas))
    historical_connected_devices = len(ips_conectadas)
    poner_num_7_display(historical_connected_devices)

## ============ Pagina Web ============
def read_file(path):
    try:
        with open(path, "rb") as f: # rb = Modo Binario
            return f.read()
    except:
        return None

def get_content_type(path):
    content_type = "text/plain"
    
    if path.endswith(".html"):
        content_type = "text/html"
    elif path.endswith(".css"):
        content_type = "text/css"
    elif path.endswith(".js"):
        content_type = "application/javascript"
    elif path.endswith(".png"):
        content_type = "image/png"
    elif path.endswith(".jpg"):
        content_type = "image/jpeg"
    elif path.endswith(".ico"):
        content_type = "image/x-icon"
    
    return content_type

def send_response(conn, status, content_type, data):
    conn.send("HTTP/1.1 {}\r\n".format(status))
    conn.send("Content-Type: {}\r\n".format(content_type))
    conn.send("\r\n")
    if data:
        conn.sendall(data)

## ============ Acciones Fetch ============
# Informacion Local del Servidor
def get_status():
    global esp32_sensor
    global broker_status
    
    # Información de la memoria flash
    stat = os.statvfs("/") # tupla
    flash_total = stat[0] * stat[2] # tam bloque * cant bloques
    flash_free = stat[0] * stat[3]
    ram_total = gc.mem_alloc() + gc.mem_free()
    ram_percent = round(gc.mem_alloc() * 100 / ram_total,1)
    
    status = { # Diccionario (clave: valor) a convertir json
        "server_wifi": wlan.isconnected(),
        "server_ip": wlan.ifconfig()[0],
        "server_wifi_signal": wlan.status("rssi"),
        "server_cpu": machine.freq(),
        "server_ram_free": gc.mem_free(),
        "server_ram_used": gc.mem_alloc(),
        "server_ram_percent": ram_percent,
        "server_flash_total": flash_total,
        "server_flash_free": flash_free,
        "server_uptime": time.ticks_ms() // 1000,
        "broker_connected": broker_status,
        "esp32_sensor_connected": esp32_sensor
    }

    return json.dumps(status) # EJ: {"wifi":true,"cpu":240000000}

logs = []
def get_events():
    global logs
    
    respuesta = json.dumps(logs)
    logs = []
    
    return respuesta
    


## ============ Socket ============

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 80)) # Establece ip y puerto
                          # Si la IP esta en blanco busca ip disponible
                          # El puerto 80 es el que usualmente se usa para el protocolo http (443 para https)
tcp_socket.listen(3) # Cant de conexiones permitidas
tcp_socket.settimeout(0.1)

## ============ Comunicacion MQTT ============
# Callback para manejo de mensajes
def mqttCallback(topic, msg):
    topic = topic.decode()
    msg = msg.decode()
    print("Mensaje recibido en ", topic, ":", msg)
    
    if topic == "igna/casa/sala/movimiento":
        event = json.loads(msg)
        logs.append(event)
    elif topic == "igna/casa/sala/status":
        global esp32_sensor
        if msg == "ONLINE":
            esp32_sensor = "Conectado"
        else:
            esp32_sensor = "No Conectado"

def mqtt_publish(data):
    client.publish(
        "igna/casa/sala/control",
        json.dumps(data)
    )
 
# Configuracion MQTT
broker = "broker.hivemq.com" 
client = MQTTClient("esp32_servidor_web", broker)
client.set_callback(mqttCallback)
client.connect()
client.subscribe("igna/casa/sala/movimiento")
client.subscribe("igna/casa/sala/status")
print("Conectado al broker MQTT")



## ============ Bucle ============
broker_status = "No Conectado"
esp32_sensor = "No Conectado"
while True:
    ## --> Obtener datos MQTT
    try:
        client.check_msg()
        broker_status = "Conectado"
    except OSError:
        broker_status = "No Conectado"
        print("Broker Desconectado")
   
    
    ## --> Nueva Conexion
    try:
        conn, addr = tcp_socket.accept() # Datos de conexion
        print("Nueva conexion desde: ", str(addr)) # IP del dispositivo conectado
        registrar_acceso(addr[0])
        ## --> Peticion HTTP
        request = conn.recv(2048).decode()
        if not request:
            conn.close()
            continue
        
        # Obtencion de Ruta
        line = request.split("\r\n")[0]
        path = line.split(" ")[1]
        
        # Logica de Acciones (Procesamiento de API primero)
        if path == "/status":
            response = get_status()
            send_response(conn, "200 OK", "application/json", response)
            print("Pedido de Status")
            conn.close()
            continue
        elif path == "/events":
            response = get_events()
            send_response(conn, "200 OK", "application/json", response)
            print("Pedido de Events")
            conn.close()
            continue
        elif path.startswith("/control"):
            print("Petición de control:", path)
            if "?" in path:
                query = path.split("?")[1] # Divide la cadena en 2 donde encuenta ? dejando (/control) (device=relay&state=1)
                params = {}
                
                for p in query.split("&"): # Divide la cadena en 2 donde encuenta & dejando (device=relay) (state=1)
                    k, v = p.split("=")
                    params[k] = v
            
                mqtt_publish(params)
            send_response(conn, "200 OK", "text/plain", "OK")

            conn.close()
            continue
        else:
            if path == "/":
                path = "/index.html"
            print("Pedido de Archivo")
        
        data = read_file(path[1:]) # 1: Elimina la '/'
        
        # Tipo de Archivo solicitado
        content_type = get_content_type(path)
        
        ## --> Retorno de Cabeceras
        if data:
            send_response(conn, "200 OK", content_type, data)
        else:
            send_response(conn, "404 Not Found", content_type, b"404 - Archivo no encontrado")
        conn.close()
    except OSError:
        pass
    finally:
        try:
            conn.close()
        except:
            pass
    

    
    
 
