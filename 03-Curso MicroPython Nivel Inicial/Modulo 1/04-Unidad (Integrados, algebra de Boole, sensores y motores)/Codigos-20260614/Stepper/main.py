from stepper import Stepper
import time

motor = Stepper(36, 39, steps_per_rev=200)


while True:
    motor.speed(20)  # modificamos la velocidad
    motor.target_deg(0)
    time.sleep(2)
    motor.target_deg(90)
    time.sleep(2)
    motor.target_deg(180)
    time.sleep(2)
    motor.target_deg(270)
    time.sleep(2)
    motor.invert_dir = False
    motor.speed(100)  # aumentamos la velocidad
    motor.step(300)
    time.sleep(2)
    motor.invert_dir = True
    motor.step(300)
    time.sleep(2)
