from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import tkinter as tk
import threading

class S(BaseHTTPRequestHandler):
    
        
    def _set_headers(self):
        self.send_response(200)
        self.send_header(keyword="Content-type", value="application/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        json_data = {"prueba": "esto es una prueba"}
        json_to_pass = json.dumps(json_data)
        self.wfile.write(json_to_pass.encode("utf-8"))
        print("json enviado")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            # Decodificar el JSON recibido desde MicroPython
            data = json.loads(post_data.decode('utf-8'))
            data = json.loads(data)
            
            # usamos los datos recibidos y los pasamos a las variables correspondientes
            S.temperatura = float(data.get('temperatura')) if data.get('temperatura') is not None else None
            S.humedad = data.get('humedad')
            S.lux = data.get('lux')
            print("Datos recibidos desde MicroPython:", data)
            print('temperatura: ' + str(self.temperatura))
            print('humedad: ' + str(self.humedad))
            print('lux: ' + str(self.lux))
            # Creamos una respuesta que puede contener cualquier informacion que deseemos
            data_to_micropython = {
                "clave1_python": "valor1_python",
                "clave2_python": "valor2_python"
            }
            response = json.dumps(data_to_micropython).encode('utf-8')

            # Configurar la respuesta HTTP
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(response)
        except json.JSONDecodeError as e:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(f'Error en el JSON recibido desde MicroPython: {str(e)}'.encode('utf-8'))



def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ("", port)  # esto hace correr el servidor en el ip local
    servidor = server_class(server_address, handler_class)
    print("Starting server....")
    servidor.serve_forever()



# Función para crear y mostrar la interfaz gráfica
def crear_interfaz():
    
    
    # Crea las etiquetas para mostrar los valores
    etiqueta_temperatura = tk.Label(ventana, text="Temperatura:")
    etiqueta_humedad = tk.Label(ventana, text="Humedad:")
    etiqueta_lux = tk.Label(ventana, text="Lux:")

    # Coloca las etiquetas en la ventana
    etiqueta_temperatura.pack()
    etiqueta_humedad.pack()
    etiqueta_lux.pack()

    # Inicia el bucle de eventos de tkinter
    ventana.mainloop()

# Función para actualizar las etiquetas en la interfaz gráfica con los valores de S
def actualizar_etiquetas():
    # Accede a las variables de instancia de la clase S
    temperatura = S.temperatura
    humedad = S.humedad
    lux = S.lux

    # Actualiza las etiquetas con los valores de S
    etiqueta_temperatura.config(text=f"Temperatura: {temperatura}")
    etiqueta_humedad.config(text=f"Humedad: {humedad}")
    etiqueta_lux.config(text=f"Lux: {lux}")

    # Programa una llamada a esta función nuevamente después de un tiempo
    ventana.after(1000, actualizar_etiquetas)


if __name__ == "__main__":
    # Configura las variables de instancia de la clase S
    S.temperatura = None
    S.humedad = None
    S.lux = None

    # Inicia el servidor en un subproceso (thread)
    server_thread = threading.Thread(target=run)
    server_thread.daemon = True
    server_thread.start()

    # Inicia la interfaz gráfica en un hilo separado (thread)
    interfaz_thread = threading.Thread(target=crear_interfaz)
    interfaz_thread.start()

    # Crea una ventana para la interfaz gráfica y sus etiquetas
    ventana = tk.Tk()
    etiqueta_temperatura = tk.Label(ventana, text="Temperatura:")
    etiqueta_humedad = tk.Label(ventana, text="Humedad:")
    etiqueta_lux = tk.Label(ventana, text="Lux:")

    # Coloca las etiquetas en la ventana
    etiqueta_temperatura.pack()
    etiqueta_humedad.pack()
    etiqueta_lux.pack()

    # Inicia la actualización de etiquetas en la interfaz gráfica
    ventana.after(1000, actualizar_etiquetas)

    # Inicia el bucle de eventos de tkinter
    ventana.mainloop()