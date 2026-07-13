from machine import Pin
import network #Librería para conectarnos con nuestro wifi
import socket  #Lo utilizamos para crear el servidor

#CLAVES DE WIFI
ssid="###############"
password="##############"
#Creamos un objeto para la conexión con el usuario y contraseña de wifi
wlan=network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

#Esperar conexión a red
while wlan.isconnected()==False:
    pass

#Revisamos datos de conexión IP
print("Conexion: ", ssid)   #Nombre de red
print(wlan.ifconfig())      #IP  

#Pin de salida del para el control de dispositivo
salida=Pin(22, Pin.OUT)

def mi_web():
    html="""
    <!Doctype html>
    <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <head>
        <body>
            <div class="container">
                <div class="row">
                    <h1>Hola Juan</h1>
                    <img src="https://sine-quo-non.com/media/aire_libre/2023/03/12/airelibre_prCubMc.png" />
                </div>
            </div>
            
        </body>
    <html>
    """
    return html

tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 80))  #Establecemos ip y puerto, 
                           #si ip está en blanco busca una ip disponible
tcp_socket.listen(3)    #Cantidad de conexiones permitidas


while True:
    conn, addr=tcp_socket.accept()                 #Datos de conexión 
    print("Nueva conexion desde: ", str(addr))     #ip del dispositivo conectado
    request=conn.recv(1024)
    print("Solicitud= ", str(request))
    request=str(request)
    
    #Condicional para la accion
    if request.find('usuario=pepe'):
        print("El usuario es Pepe") 
    
    response=mi_web()
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-Type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()