from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import tkinter as tk
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
            
            # Hacer algo con los datos recibidos desde MicroPython
            S.temperatura = float(data.get('temperatura')) if data.get('temperatura') is not None else None
            S.humedad = data.get('humedad')
            S.lux = data.get('lux')
            print("Datos recibidos desde MicroPython:", data)
            print('temperatura: ' + str(self.temperatura))
            print('humedad: ' + str(self.humedad))
            print('lux: ' + str(self.lux))
            # Crear una respuesta JSON para enviar a MicroPython
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

# Declarar temperatura_data como variable global
temperatura_data = [0]
bar = None
canvas = None
# Función para crear y mostrar la interfaz gráfica
def crear_interfaz():
    global canvas, bar
   
    # Crea las etiquetas para mostrar los valores
    etiqueta_temperatura = tk.Label(ventana, text="Temperatura:")

    # Crea un lienzo (Canvas) para el gráfico
    canvas = tk.Canvas(ventana, width=400, height=200)
    canvas.pack()

    # Inicializa el gráfico de barras
    fig, ax = plt.subplots(figsize=(3, 1.5))
    bar = ax.bar(["Temperatura"], temperatura_data)
    ax.set_ylim(0, 40)  # Puedes ajustar los límites según tus datos

    # Configura el lienzo para el gráfico
    canvas = FigureCanvasTkAgg(fig, master=canvas)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Programa una llamada a la función de actualización del gráfico
    ventana.after(1000, actualizar_grafico)
    # Coloca las etiquetas en la ventana
    etiqueta_temperatura.pack()
    etiqueta_humedad.pack()
    etiqueta_lux.pack()
    # Inicia el bucle de eventos de tkinter
    ventana.mainloop()
def actualizar_grafico():
    bar[0].set_height(temperatura_data[0])
    canvas.draw()
# Función para actualizar las etiquetas y el gráfico con los valores de S
def actualizar_valores():
    global temperatura_data  # Accede a la variable global
    global bar  # Accede a la variable global

    # Accede a las variables de instancia de la clase S
    temperatura = S.temperatura
    humedad = S.humedad
    lux = S.lux

    # Actualiza las etiquetas con los valores de S
    etiqueta_temperatura.config(text=f"Temperatura: {temperatura}")
    etiqueta_humedad.config(text=f"Humedad: {humedad}")
    etiqueta_lux.config(text=f"Lux: {lux}")

    # Actualiza los datos de temperatura para el gráfico
    temperatura_data[0] = temperatura

    if bar is not None:  # Verifica si bar no es None antes de acceder a él
        bar[0].set_height(temperatura_data[0])
        canvas.draw()
    
    # Programa una llamada a esta función nuevamente después de un tiempo
    ventana.after(1000, actualizar_valores)


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
    
    canvas = tk.Canvas(ventana, width=400, height=200)
    canvas.pack()
    fig, ax = plt.subplots(figsize=(3, 1.5))
    bar = ax.bar(["Temperatura"], temperatura_data)
    ax.set_ylim(0, 40)  # Puedes ajustar los límites según tus datos

    # Configura el lienzo para el gráfico
    canvas = FigureCanvasTkAgg(fig, master=canvas)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    
    # Función para actualizar el gráfico y los valores de los dispositivos
    def actualizar_datos_y_grafico():
        actualizar_valores()  # Actualiza los valores de los dispositivos
        actualizar_grafico()  # Actualiza el gráfico
    # Inicia la actualización de etiquetas y el gráfico en la interfaz gráfica
    ventana.after(1000, actualizar_datos_y_grafico)


    # Inicia el bucle de eventos de tkinter
    ventana.mainloop()
