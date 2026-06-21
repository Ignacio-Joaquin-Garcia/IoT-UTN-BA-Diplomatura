from machine import Pin
from time import sleep

pin_a=Pin(22, Pin.OUT)
pin_b=Pin(23, Pin.OUT)
pin_c=Pin(14, Pin.OUT)
pin_d=Pin(12, Pin.OUT)
pin_e=Pin(13, Pin.OUT)
pin_f=Pin(5, Pin.OUT)
pin_g=Pin(18, Pin.OUT)
pin_dp=Pin(26, Pin.OUT)

H=0
L=1
numero=3

def led(a, b, c, d, e, f, g, dp):
  pin_a.value(a)
  pin_b.value(b)
  pin_c.value(c)
  pin_d.value(d)
  pin_e.value(e)
  pin_f.value(f)
  pin_g.value(g)
  pin_dp.value(dp)

def valor(numero):
  if numero==0:
    led(H, H, H, H, H, H, L, L)
  if numero==1:
    led(L, H, H, L, L, L, L, L)
  if numero==2:
    led(H, H, L, H, H, L, H, L)
  if numero==3:
    led(H, H, H, H, L, L, H, L)
  if numero==4:
    led(L, H, H, L, L, H, H, L)
  if numero==5:
    led(H, L, H, H, L, H, H, L)
  if numero==6:
    led(H, L, H, H, H, H, H, L)
  if numero==7:
    led(H, H, H, L, L, L, L, L)
  if numero==8:
    led(H, H, H, H, H, H, H, L)
  if numero==9:
    led(H, H, H, H, L, H, H, L)

valor(numero)