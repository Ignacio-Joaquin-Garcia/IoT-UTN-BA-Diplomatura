from machine import Pin
from machine import Timer
import mfrc522

led = Pin(2, Pin.OUT)
led.on()

lector = mfrc522.MFRC522(14, 13, 12, 5, 4)


def leertag():
    led.value(not led.value)
    tagvalue = lector.getCardValue()
    if tagvalue != "":
        if tagvalue == "0x57e4f60c":
            print("autorizado nivel 1")
        elif tagvalue == "0x57fc300c":
            print("autorizado nivel 2")
        else:
            print("no autorizado")


tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: leertag())
