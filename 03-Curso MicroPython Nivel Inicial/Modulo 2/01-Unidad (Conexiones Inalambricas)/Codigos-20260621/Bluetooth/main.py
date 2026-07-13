import bluetooth
from BLE import BLEUART
import time
from machine import Pin, PWM
from utime import sleep


motora = Pin(32, Pin.OUT)
motorb = PWM(Pin(33), freq=20000, duty=0)

# inicializamos el bluetooth

nombre = "ESP32"
ble = bluetooth.BLE()
uart = BLEUART(ble, nombre)


# recepcion de datos
def al_recibir():
    rx_buffer = uart.read().decode().strip()
    uart.write("mensaje recibido \n")
    if rx_buffer == "derecha":
        derecha()
        uart.write("girando a la derecha \n")
    elif rx_buffer == "izquierda":
        izquierda()
        uart.write("girando a la izquierda \n")
    elif rx_buffer == "alto":
        alto()
        uart.write("detenido \n")


# registrar evento de bluetooth
uart.irq(handler=al_recibir)


def derecha():
    Pin.on(motora)
    motorb.duty(512)
    print("derecha")
    print("50%")
    sleep(1)


def izquierda():
    Pin.off(motora)
    motorb.duty(512)
    print("izquierda")
    print("50%")
    sleep(1)


def alto():
    Pin.off(motora)
    motorb.duty(0)
