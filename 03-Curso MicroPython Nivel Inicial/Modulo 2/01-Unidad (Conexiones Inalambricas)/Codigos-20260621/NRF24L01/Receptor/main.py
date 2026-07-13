# Codigo receptor

import usys
import ustruct as struct
import utime
from machine import Pin, SPI, SoftSPI
from nrf24l01 import NRF24L01
from micropython import const

# delay between receiving a message and waiting for the next message
POLL_DELAY = const(15)
# Delay between receiving a message and sending the response
# (so that the other pico has time to listen)
SEND_DELAY = const(10)


if usys.platform == "esp8266":  # Hardware SPI
    spi = SPI(1)  # miso : 12, mosi : 13, sck : 14
    cfg = {"spi": spi, "csn": 15, "ce": 2}
elif usys.platform == "esp32":  # Software SPI
    spi = SoftSPI(sck=Pin(25), mosi=Pin(33), miso=Pin(32))
    cfg = {"spi": spi, "csn": 26, "ce": 27}
else:
    raise ValueError("Unsupported platform {}".format(usys.platform))
# Addresses
pipes = (b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0")

csn = Pin(cfg["csn"], mode=Pin.OUT, value=1)
ce = Pin(cfg["ce"], mode=Pin.OUT, value=0)
spi = cfg["spi"]
nrf = NRF24L01(spi, csn, ce, payload_size=16)

nrf.open_tx_pipe(pipes[1])
nrf.open_rx_pipe(1, pipes[0])
nrf.start_listening()

print("nRF24L01 receiver; waiting for the first post...")

while True:
    if nrf.any():  # we received something
        while nrf.any():
            buf = nrf.recv()
            temperatura, humedad, lux = struct.unpack("fff", buf)
            print("mensaje recibido:")
            print("Temperatura: " + str(temperatura))
            print("Humedad: " + str(humedad))
            print("lux: " + str(lux))
            utime.sleep_ms(POLL_DELAY)  # delay before next listening

        utime.sleep_ms(SEND_DELAY)  # Give the other node a brief time to listen
        nrf.stop_listening()
        try:
            nrf.send(struct.pack("8s", "recibido"))
        except OSError:
            pass
        print("enviando confirmacion de recepcion ", "recibido")
        nrf.start_listening()
