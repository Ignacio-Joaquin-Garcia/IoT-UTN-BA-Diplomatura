import pyfirmata
from pyfirmata import Arduino, util, OUTPUT, PWM
import time

objetoArduino = Arduino('COM5')

it = util.Iterator(objetoArduino)
it.start()

pinAnalogico = objetoArduino.get_pin('a:0:i')

objetoArduino.digital[5].mode = OUTPUT
objetoArduino.digital[6].mode = PWM

flagEstado = True
estado = -1

while True:
    opcion = int(input("\n1) para cambiar el estado de un led \n2) para imprimir el valor del potenciometro a un led\nDato: "))

    if opcion == 1:
        while flagEstado == True:
            estado = int(input("Ingresar el estado: "))
            if estado == 0 or estado == 1:
                objetoArduino.digital[5].write(int(estado))
                flagEstado = False
            time.sleep(1)

    elif opcion == 2:
        valor = pinAnalogico.read()
        objetoArduino.digital[6].write(valor)
        print("estado analogico: " + str(valor))

    time.sleep(1)
    flagEstado = True