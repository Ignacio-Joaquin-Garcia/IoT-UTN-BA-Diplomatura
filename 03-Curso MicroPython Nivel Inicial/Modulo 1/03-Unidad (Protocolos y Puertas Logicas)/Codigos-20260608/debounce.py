from machine import Pin
import time

# definiciones
led_externo_rojo=Pin(22, Pin.OUT)
pulsador=Pin(14, Pin.IN, pull=Pin.PULL_UP)

estado_led=1
estado_boton=0 #POR AHORA NO USADA
ultimo_estado_de_boton=0
ultimo_tiempo_de_rebote=0
delay_por_rebote=50


while True:
    lectura=pulsador.value()
    if lectura!=ultimo_estado_de_boton:
        ultimo_tiempo_de_rebote=time.ticks_ms()
        print(">>>>>>>>",ultimo_tiempo_de_rebote)
    if time.ticks_ms()-ultimo_tiempo_de_rebote>delay_por_rebote:
      if lectura!=estado_boton:
          estado_boton=lectura
          if estado_boton==1:
              if estado_led==1:
                  estado_led=0
              elif estado_led==0:
                  estado_led=1

    led_externo_rojo.value(estado_led)
    ultimo_estado_de_boton=lectura