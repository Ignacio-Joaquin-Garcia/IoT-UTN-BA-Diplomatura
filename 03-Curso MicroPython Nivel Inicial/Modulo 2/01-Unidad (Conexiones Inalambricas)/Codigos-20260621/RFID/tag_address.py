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
        print(tagvalue)


tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: leertag())
