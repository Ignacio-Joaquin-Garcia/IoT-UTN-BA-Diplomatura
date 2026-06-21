#Librerias
from machine import Pin, Timer
import time
#Pines
readRelay = Pin(22, Pin.IN)
writeRelay = Pin(23, Pin.OUT)
#Variables Iniciales
writeRelayStatus = False

#Funciones
def changeRelayStatus():
    global writeRelayStatus
    writeRelayStatus = not writeRelayStatus
    writeRelay.value(writeRelayStatus) 
#Start
     #Timers
tim_0 = Timer(0)
tim_0.init(period = 2000, mode=Timer.PERIODIC, callback=lambda t:changeRelayStatus())
writeRelay.value(1)

#Loop
while True:
    print("Estado readRelaY: ", readRelay.value())
    time.sleep_ms(500)
    
    
    

