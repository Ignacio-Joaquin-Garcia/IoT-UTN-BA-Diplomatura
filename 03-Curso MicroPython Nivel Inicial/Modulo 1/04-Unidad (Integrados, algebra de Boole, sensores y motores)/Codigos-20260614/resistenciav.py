from machine import Pin
import time
import math
from machine import ADC
from machine import PWM

pwm=PWM(Pin(22), freq=500, duty=0)
potenciometro=ADC(Pin(14))
potenciometro.atten(ADC.ATTN_11DB)


while True:
  valor=potenciometro.read()
  valor=math.trunc(valor/4)
  pwm.duty(valor)
  print(
    potenciometro.read_u16(), 
    " -- ", 
    potenciometro.read(), 
    " -- ", 
    potenciometro.read_uv(), 
    " -- ", 
    valor
  ) 
  time.sleep(.5)