## ============ Librerias ============
from machine import Pin, PWM
import time
import json
# Comunicacion Externa
import network
from umqtt.simple import MQTTClient
# Hora Real
import ntptime


## ============ Config Dispositivos Internos ============
esp32LedPin = Pin(2, Pin.OUT)
movementSensorPin = Pin(36, Pin.IN)
# Espera -> Configuracion Sensor 
"""
for _ in range(0, 80):
    esp32LedPin.on()
    time.sleep_ms(500)
    esp32LedPin.off()
    time.sleep_ms(500)
"""

# Dispositivos controlables externamente
relayPin = Pin(15, Pin.OUT)
relayPin.off()
redPin = Pin(25, Pin.OUT)
greenPin = Pin(33, Pin.OUT)
bluePin = Pin(32, Pin.OUT)
buzzerPin = PWM(Pin(26))
buzzerPin.freq(1000)
buzzerPin.duty(0)




## ============ Config Comunicacion Externa ============
# WI-FI 
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

# Obtener Hora
ntptime.settime() 
def get_argentina_time():
    argentina_timestamp = time.time() - 3*3600

    year, month, day, hour, minute, second, _, _ = time.localtime(argentina_timestamp)

    return "{:02d}/{:02d}/{} {:02d}:{:02d}:{:02d}".format(
        day,
        month,
        year,
        hour,
        minute,
        second
    )

# MQTT
def mqtt_callback(topic, msg):
    try:
        topic = topic.decode()
        data = json.loads(msg.decode())
        if topic == "igna/casa/sala/control":
            if data["device"] == "relay":
                relayPin.value(int(data["state"]))
            elif data["device"] == "redLed":
                redPin.value(int(data["state"]))
            elif data["device"] == "greenLed":
                greenPin.value(int(data["state"]))
            elif data["device"] == "blueLed":
                bluePin.value(int(data["state"]))
            elif data["device"] == "buzzer":
                buzzerPin.freq(int(data["freq"]))
                buzzerPin.duty(int(data["state"]) * 4)
                
    except Exception as e:
        print("Error MQTT:", e)

def mqtt_publish():
    # Envia Movimiento del sensor
    event = {
        "time": get_argentina_time(),
        "sensor": "Sala",
        "type": "Movimiento"
    }
    
    client.publish(
        "igna/casa/sala/movimiento",
        json.dumps(event)
    )

broker = "broker.hivemq.com" 
client = MQTTClient("esp32_sensores", broker)

client.set_callback(mqtt_callback)
client.set_last_will(
    "igna/casa/sala/status",
    "OFFLINE"
)

client.connect()
print("Conectado al MQTT")

# Suscripcion a topicos MQTT
client.subscribe("igna/casa/sala/control")


# Enviamos que el dispositivo esta listo
client.publish(
    "igna/casa/sala/status",
    "ONLINE"
)

## ============ Bucle ============
last_movement_state = 0 # Flag
while True:
    client.check_msg()
    
    movement = movementSensorPin.value()
    
    if movement:
        esp32LedPin.on()
    else:
        esp32LedPin.off()
    
    if movement == 1 and last_movement_state == 0:
        print("Persona Detectada")
        # Enviar info MQTT
        mqtt_publish()
    last_movement_state = movement
    time.sleep_ms(100)

    
    