import pyfirmata
from pyfirmata import Arduino, util, OUTPUT, INPUT, PWM, SERVO
import time
objetoArduino = Arduino('COM5')
it = util.Iterator(objetoArduino)
it.start()
pinAnalogico = objetoArduino.get_pin('a:0:i')
objetoArduino.digital[5].mode = 1

while True:
	valor = pinAnalogico.read()
	objetoArduino.digital[5].write(1)
	print("Estado analogico: " + str(valor))
	time.sleep(1)