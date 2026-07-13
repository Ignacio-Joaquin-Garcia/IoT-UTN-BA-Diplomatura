import time
from umqttsimple import MQTTClient
import machine
import network
import esp

esp.osdebug(None)
import gc

gc.collect()

ssid = "megatronica.wifi"
password = "megawifi23"
mqtt_server = "broker.hivemq.com"

client_id = "emisor"
topic_sub = b"saludo"
topic_pub = b"confirmacion"


last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print("conexion establecida")
print(station.ifconfig())
