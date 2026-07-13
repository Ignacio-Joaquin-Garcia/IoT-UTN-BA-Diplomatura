import esp32
from machine import Pin
from machine import deepsleep
from time import sleep

# En el ESP-32 se pueden usar los pines GPIO 0 y GPIO 3  al GPIO 16

wake1 = Pin(14, mode=Pin.IN)

# level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW
esp32.wake_on_ext0(pin=wake1, level=esp32.WAKEUP_ANY_HIGH)
# si usamos el ext1 en vez del cero, podemos usar mas de un pin para despertar el ESP


print("despierto, activando deep sleep en 5 segundos")
sleep(1)
print("4 segundos")
sleep(1)
print("3 segundos")
sleep(1)
print("2 segundos")
sleep(1)
print("1 segundos")
sleep(1)
print("activando deep sleep")
deepsleep()
