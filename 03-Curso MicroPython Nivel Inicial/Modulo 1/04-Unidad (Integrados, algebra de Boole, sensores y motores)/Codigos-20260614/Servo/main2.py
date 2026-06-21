import time
from servo import Servo


servo = Servo(pin_id=13)
servo.write(30)
time.sleep(2.0)
servo.write(60)
time.sleep(2.0)
servo.write(90)
