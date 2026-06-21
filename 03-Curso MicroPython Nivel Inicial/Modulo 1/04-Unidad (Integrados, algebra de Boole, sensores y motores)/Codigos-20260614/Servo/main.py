from machine import Pin, PWM

from time import sleep

 

pinServo = Pin(13)

servo = PWM(pinServo, freq=50)

 

while True:

    servo.duty(40)  

    sleep(1)

    servo.duty(77)  

    sleep(1)

    servo.duty(115)  

    sleep(1)