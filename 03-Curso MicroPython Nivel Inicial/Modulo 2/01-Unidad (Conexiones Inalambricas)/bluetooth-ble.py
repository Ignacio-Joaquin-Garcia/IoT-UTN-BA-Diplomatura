print("Paso 0")
from micropython import const
import machine
import time
import dht
import bluetooth

### Initializing Electronical / Hardware Components
print("Paso 1")
d = dht.DHT22(machine.Pin(4))

# --------------------------------------
print("Paso 2")
### Registrying a new Profile -> Service for Bluetooth BLE
bluetooth_name = "TX-Igna-ESP32-BLE"
## UUIDs from different services
# 1. Container Services
SERVICE_UUID = bluetooth.UUID('4fafc201-1fb5-459e-8fcc-c5c9c331914b')
# 2. Characteristic UUIDs
TEMP_CHAR_UUID = bluetooth.UUID('beb5483e-36e1-4688-b7f5-ea07361b26a8')
HUM_CHAR_UUID = bluetooth.UUID('beb5483e-36e1-4688-b7f5-ea07361b26b9')

## Characteristics
TEMP_CHAR = (TEMP_CHAR_UUID, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY)
HUM_CHAR = (HUM_CHAR_UUID, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY)

## Service Register -> (Service UUID, Characteristics)
SERVICES = ((SERVICE_UUID, (TEMP_CHAR, HUM_CHAR)),)

# --------------------------------------
print("Paso 3")
### Defining Notify Function to send the services
## events -> BLE(irq)
_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
## Saving the conection
conn_handle = None
def ble_irq(event, data):
    global conn_handle

    if event == _IRQ_CENTRAL_CONNECT:
        conn_handle, addr_type, addr = data
        print("Cliente conectado")

    elif event == _IRQ_CENTRAL_DISCONNECT:
        print("Cliente desconectado")
        conn_handle = None
        # Start Advertising for another device to connect
        ble.gap_advertise(100, adv_data)

# --------------------------------------
print("Paso 4")
### Start Bluetooth Conection
## Start BLE and Register Services (GATT Server)
# Start Object BLE
print("4.1")
ble = bluetooth.BLE()
# BLE Active
print("4.2")
ble.active(True)
# Register Services
print("4.3")
handles = ble.gatts_register_services(SERVICES)

print("4.4")
temp_handle = handles[0][0]
hum_handle = handles[0][1]
# Register Notify Callback
print("4.5")
ble.irq(ble_irq)


print("Paso 5")
## Advertising -> being visible for a device to connect
# 0x02 = Camp Longitude
# 0x01 = Type: Flags
# 0x06 = Flag Values
# 0x09 = Complete Name
adv_data = bytes([0x02, 0x01, 0x06]) + bytes([len(bluetooth_name) + 1, 0x09]) + bluetooth_name.encode()

# Start Advertising
ble.gap_advertise(100, adv_data) # (100 Microseconds = 16 transmission * 1 second of 20 bytes per transmission)
print("Dispositivo BLE anunciando como:", bluetooth_name)

### Loop
print("Paso 6")
print("Inicio")
temperature = 25.0
humidity = 60.0
while True:
    ## Measure
    #d.measure()

    temperature += 0.1
    humidity += 0.2


    ## Read
    ble.gatts_write(temp_handle, str(temperature).encode())
    ble.gatts_write(hum_handle, str(humidity).encode())

    ## Notify
    if conn_handle is not None:
        ble.gatts_notify(conn_handle, temp_handle)
        ble.gatts_notify(conn_handle, hum_handle)

    ## Sleep between advertising
    time.sleep(1)