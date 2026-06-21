

from machine import Pin
from machine import I2C
from lcd_i2c import LCD

sda=Pin(21, Pin.OUT)
scl=Pin(22, Pin.OUT)


NUM_ROWS = 2
NUM_COLS = 16


####### Obtenemos la dirección del LCD

i2c=I2C(0, sda=sda, scl=scl, freq=400000)


decimal_i2c=i2c.scan()
hexadecimal_i2c=hex(decimal_i2c[0])


def decimal_a_binario(decimal): 
    binario=0
    i=0
    while(decimal>0):
        digito=decimal%2
        decimal=int(decimal//2)
        binario=binario+digito(10*i)
        i=i+1
    return binario


binario_i2c=decimal_a_binario(decimal_i2c[0])
print("Dirección del lcd en decimal, hexadecimal y binario")
print("Decimal: ", decimal_i2c, "Hexadecimal: ", hexadecimal_i2c, "Binario: ", binario_i2c, end="\n\n")


######### CONFIGURAMOS I2C

lcd = LCD(addr=int(hexadecimal_i2c), cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)


lcd.begin()
lcd.print("Hola Mundo")



creacion de caracteres

lcd.create_char(
    location=0,
    charmap=[0x00, 0x00, 0x11, 0x04, 0x04, 0x11, 0x0E, 0x00]
    # this is the binary matrix, feel it, see it
    # 00000
    # 00000
    # 10001
    # 00100
    # 00100
    # 10001
    # 01110
    # 00000
)
print("Create custom char ':-)'")

show custom char stored at location 0

lcd.set_cursor(0,2)
lcd.print(chr(0))
lcd.set_cursor(2,2)
lcd.print("cursor personalizado")