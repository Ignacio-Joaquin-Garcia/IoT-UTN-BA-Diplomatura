from machine import Pin, PWM
from utime import sleep

motora = Pin(32, Pin.OUT)
motorb = PWM(Pin(33), freq=20000, duty=512)


def derecha():
    Pin.on(motora)
    motorb.duty(1023)
    print("derecha")
    print("0%")
    sleep(1)
    motorb.duty(768)
    print("25%")
    sleep(1)
    motorb.duty(512)
    print("50%")
    sleep(1)
    motorb.duty(256)
    print("75%")
    sleep(1)
    motorb.duty(0)
    print("100%")
    sleep(1)


def izquierda():
    Pin.off(motora)
    motorb.duty(0)
    print("izquierda")
    print("0%")
    sleep(1)
    motorb.duty(256)
    print("25%")
    sleep(1)
    motorb.duty(512)
    print("50%")
    sleep(1)
    motorb.duty(768)
    print("75%")
    sleep(1)
    motorb.duty(1023)
    print("100%")
    sleep(1)


while True:
    izquierda()
    sleep(2)
    derecha()

# please note how setting the input pins relates to how the output power to the motor
# truth.JPG
# truth.JPG (22.02 KiB) Viewed 5106 times
# as you can see when ever the 2 input pins are the same the motor is off and when ever they are different the motor spin and it will spin depending upon the order of which 1 high and which 1 is low.

# Software: I use 1 pin as direction pin and the other pin as speed pin. If the direction is low then the motor will get power when ever the speed pin is high so the speed the motor will spin at will be the duty with of the speed pin i.e PWM_duty = desired_speed. If the direction is high then motor will spin the other way and the motor will get power anytime the speed pin is low so you have to invert the PWM duty i.e PWM_duty = 100 - desired_speed
# Top
