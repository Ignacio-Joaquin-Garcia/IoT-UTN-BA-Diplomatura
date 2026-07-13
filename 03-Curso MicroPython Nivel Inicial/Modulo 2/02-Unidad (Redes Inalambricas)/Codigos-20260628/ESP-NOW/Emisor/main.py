import network
import espnow
from machine import Pin, I2C
from bh1750 import BH1750
import ahtx0
from utime import sleep

scl = Pin(5)
sda = Pin(4)
i2c = I2C(scl, sda)

luz = BH1750(i2c)
# Create the sensor object using I2C
sensor = ahtx0.AHT10(i2c)


# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()  # For ESP8266

e = espnow.ESPNow()
e.active(True)
peer = b"\x48\x3f\xda\x47\x92\xde"  # MAC address of peer's wifi interface
e.add_peer(peer)  # Must add_peer() before send()

while True:
    print("enviando...")
    e.send(peer, "Nuevo dato")
    e.send(peer, "Temperatura: %0.2f C" % sensor.temperature)
    e.send(peer, "Humedad: %0.2f %%" % sensor.relative_humidity)
    e.send(peer, "lux: %0.2f LUX" % luz.luminance(BH1750.ONCE_HIRES_1))
    print("enviado")
    sleep(5)
