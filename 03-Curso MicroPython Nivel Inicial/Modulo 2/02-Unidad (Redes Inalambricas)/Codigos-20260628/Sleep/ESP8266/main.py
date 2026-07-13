import machine
from machine import Pin
from time import sleep

# Para que este codigo funcione debemos conectar el PIN 16 al PIN RST sino, no se despertara nunca

led = Pin(2, Pin.OUT)


def deep_sleep(msecs):
    # configurando alarma
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    # estableciendo la alarma para que despierte luego del intervalo seleccionado
    rtc.alarm(rtc.ALARM0, msecs)

    # acivar el deep sleep
    machine.deepsleep()


# parpadear
led.value(1)
sleep(1)
led.value(0)
sleep(1)

# esperando para que se establezca una conexion serial
sleep(5)

print("despierto, activando deep sleep...")

# deep sleep por 10 segundos (10000 mili)
deep_sleep(10000)
