from machine import Pin
from time import sleep

clk=Pin(22, Pin.IN)
dt=Pin(23, Pin.IN)
sw=Pin(14, Pin.IN, Pin.PULL_UP)


last_clk = 0
last_dt = 0
last_value = 0
valor=True # POR DEFECTO SIEMPRE ESTÁ EN ALTO DEBIDO A LAS RESISTENCIAS DE PULL_UP
pulsado=False


while True:
    #VER SI SE HA GIRADO EL CODIFICADOR ROTATORIO
    if ( clk.value()!= last_clk or dt.value() != last_dt or sw.value()!= last_sw):
        print(clk.value(), dt.value(), sw.value())
        last_clk = clk.value()
        last_dt = dt.value()
        last_sw = sw.value()
    #VER SI SE HA GIRADO
    if valor!=clk.value(): #VEO SI CAMBIA EL ESTADO DE CLK
        if clk.value()==False:
            if dt.value()==False:
                print(">>>>>>>>>>>>>>>>>>>> : Sentido ANTI horario" )
                sleep(0.5)
            else:
                print(">>>>>>>>>>>>>>>>>>>> : Sentido horario" )
                sleep(0.5)
    #DETECTAR PRESIÓN DE BOTÓN
    if sw.value()==False and pulsado==False:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>El sw está presionado")
        sleep(0.5)
        pulsado=True
    if sw.value()==True and pulsado==True:
        pulsado=False