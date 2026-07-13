import usocket as socket
import network


# import gc
# gc.collect()

ssid = "Ejemplo_AP"
password = "012345678"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
    pass

print("conectado")
print(ap.ifconfig())


def web_page():
    html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Hello, World!</h1></body></html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("coneccion de  %s" % str(addr))
    request = conn.recv(1024)
    print("Contenido = %s" % str(request))
    conn.send(web_page())
    conn.close()
