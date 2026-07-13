# Codigo emisor
import usys
import ustruct as struct
import utime
from machine import Pin, SPI, SoftSPI, I2C
from bh1750 import BH1750
import ahtx0
from nrf24l01 import NRF24L01


if usys.platform == "esp8266":  # Hardware SPI
    spi = SPI(1)  # miso : 12, mosi : 13, sck : 14
    cfg = {"spi": spi, "csn": 15, "ce": 2}
elif usys.platform == "esp32":  # Software SPI
    spi = SoftSPI(sck=Pin(25), mosi=Pin(33), miso=Pin(32))
    cfg = {"spi": spi, "csn": 26, "ce": 27}
else:
    raise ValueError("Unsupported platform {}".format(usys.platform))

# hay que hacer una mencion a las direcciones
# Addresses are in little-endian format. They correspond to big-endian
# 0xf0f0f0f0e1, 0xf0f0f0f0d2
pipes = (b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0")

print("NRF24L01 transmitter")

csn = Pin(cfg["csn"], mode=Pin.OUT, value=1)
ce = Pin(cfg["ce"], mode=Pin.OUT, value=0)
spi = cfg["spi"]
nrf = NRF24L01(spi, csn, ce, payload_size=16)

nrf.open_tx_pipe(pipes[0])
nrf.open_rx_pipe(1, pipes[1])
nrf.start_listening()

scl = Pin(5)
sda = Pin(4)
i2c = I2C(scl, sda)

luz = BH1750(i2c)
# Create the sensor object using I2C
sensor = ahtx0.AHT10(i2c)

while True:
    # Stop listening, time to send a message
    nrf.stop_listening()
    temperatura = sensor.temperature
    humedad = sensor.relative_humidity
    lux = luz.luminance(BH1750.ONCE_HIRES_1)
    print("sending:")
    print("Temperatura: " + str(temperatura))
    print("Humedad: " + str(humedad))
    print("lux: " + str(lux))

    try:
        nrf.send(
            struct.pack(
                "fff",
                temperatura,
                humedad,
                lux,
            )
        )  # sending the message
        # hay que explicar que significa la "i" (int)
    except OSError:
        pass

    # Listen if the other node answers us
    nrf.start_listening()

    # Wait for 250ms max
    start_time = utime.ticks_ms()
    timeout = False
    while not nrf.any() and not timeout:
        if utime.ticks_diff(utime.ticks_ms(), start_time) > 250:
            timeout = True

    if timeout:  # no response received
        print("failure, no response")

    else:  # a response has been received
        (response,) = struct.unpack("8s", nrf.recv())
        print("confirmacion de recepcion:", str(response, "utf-8"))

    # Wait a second before sending the next message
    utime.sleep_ms(1000)
