from machine import deepsleep
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

# parpadear
led.value(1)
sleep(1)
led.value(0)
sleep(1)

# esperando para que se establezca una conexion serial
sleep(5)

print("despierto, activando deep sleep...")

# deep sleep por 10 segundos (10000 mili)
deepsleep(10000)
