import network
import espnow
import ubinascii

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
wlan_mac = sta.config("mac")
print(ubinascii.hexlify(wlan_mac).decode())
sta.disconnect()  # Because ESP8266 auto-connects to last Access Point

e = espnow.ESPNow()
e.active(True)

while True:
    host, msg = e.recv()
    if msg:  # msg == None if timeout in recv()
        print(msg)
