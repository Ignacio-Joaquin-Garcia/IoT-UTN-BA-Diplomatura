import gc
import machine
import network

def connect_wlan(ssid, password):
    
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    ap_if.active(False)

    if not sta_if.isconnected():
        print("Connecting to WLAN ({})...".format(ssid))
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            print("conectando")
        print("configuracion de red:", sta_if.ifconfig())

    return True


def main():
    

    gc.collect()
    gc.enable()

    # Wi-Fi credentials
    SSID = "CLAROWIFI"
    PASSWORD = "11557788"

    connect_wlan(SSID, PASSWORD)



if __name__ == "__main__":
    main()