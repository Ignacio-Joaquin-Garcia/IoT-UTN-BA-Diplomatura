import serial
import time
miConexion = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

def write_read(x):
	miConexion.write((x + "\n").encode('utf-8'))
	time.sleep(0.05)
	data = miConexion.readline()
	return data
	
while True:
	num = input("Enter a number: ")
	value = write_read(num)
	print(value)