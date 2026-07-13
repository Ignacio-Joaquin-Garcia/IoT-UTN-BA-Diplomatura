## ============ Librerias ============
from machine import Pin
import machine
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
#redPin = Pin(0, Pin.OUT)
#greenPin = Pin(0, Pin.OUT)
#bluePin = Pin(0, Pin.OUT)
#buzzerPin = Pin(0, Pin.OUT)





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
    # Enciende lo que le pidan por mqtt
    try:
        topic = topic.decode()
        data = json.loads(msg.decode())

        if topic == "igna/casa/sala/control":
            if data["device"] == "relay":
                relayPin.value(data["state"])

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
    if movement == 1 and last_movement_state == 0:
        print("Persona Detectada")
        esp32LedPin.on()
        # Enviar info MQTT
        mqtt_publish()
    last_movement_state = movement
    time.sleep_ms(500)
    esp32LedPin.off()
    
    # Cuando no hay movimiento duerme
    time.sleep(5)
    esp32.wake_on_ext0(
        pin=movementSensorPin,
        level=machine.WAKEUP_ANY_HIGH
    )
    machine.deepsleep()