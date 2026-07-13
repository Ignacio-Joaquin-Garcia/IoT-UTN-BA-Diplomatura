from machine import Pin
from time import sleep
import senko

led = Pin(2, Pin.OUT)

version = "1.0.0"
OTA = senko.Senko(user="maxhuyk", repo="ota", files=["boot.py", "main.py"])

while True:
    # parpadear
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
    if OTA.fetch():
        print("A newer version is available!")
        machine.reset()
    else:
        print("Up to date!")
        print(version)
