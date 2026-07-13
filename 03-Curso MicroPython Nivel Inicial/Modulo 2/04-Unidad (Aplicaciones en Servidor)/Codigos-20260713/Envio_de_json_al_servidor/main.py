import urequests
from machine import Pin, I2C, Timer
from bh1750 import BH1750
import ahtx0
from utime import sleep
import ujson

scl = Pin(5)
sda = Pin(4)
i2c = I2C(scl, sda)

luz = BH1750(i2c)
# Create the sensor object using I2C
sensor = ahtx0.AHT10(i2c)

# URL de destino
url = 'http://192.168.100.4'


def post():
    # Realizar una solicitud POST con las variables
    data =  ujson.dumps({
    'temperatura': str(sensor.temperature),
    'humedad': str(sensor.relative_humidity),
    'lux': str(luz.luminance(BH1750.ONCE_HIRES_1)),
    })
    response = urequests.post(url, json=data)
    # Verificar la respuesta
    if response.status_code == 200:
        print('Solicitud POST exitosa')
        print(response.text)
    else:
        print("Error: Request failed with status code", response.status_code)
        print(response.text)  # Print the response content for debugging purposes

    # Cierra la conexión
    response.close()

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: post())


