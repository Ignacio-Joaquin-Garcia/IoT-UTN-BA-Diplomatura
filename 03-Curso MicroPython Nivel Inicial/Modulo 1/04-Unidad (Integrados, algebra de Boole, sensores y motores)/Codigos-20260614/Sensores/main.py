from machine import Pin, I2C
from bh1750 import BH1750
import ahtx0
from utime import sleep

scl = Pin(5)
sda = Pin(4)
i2c = I2C(scl, sda)

luz = BH1750(i2c)
# Create the sensor object using I2C
sensor = ahtx0.AHT10(i2c)

while True:
    print("\nTemperatura: %0.2f °C" % sensor.temperature)
    print("Humedad: %0.2f %%" % sensor.relative_humidity)
    print("lux: %0.2f LUX" % luz.luminance(BH1750.ONCE_HIRES_1))
    sleep(5)
