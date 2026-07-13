from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import tkinter as tk
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os  # Importa la biblioteca os
from peewee import *
import datetime  # Importa la biblioteca datetime

# Directorio actual del script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Ruta completa al archivo de la base de datos
database_path = os.path.join(current_directory, 'mi_base_de_datos.db')

# Configura la base de datos con la ruta completa
db = SqliteDatabase(database_path)

class LecturaSensor(Model):
    temperatura = FloatField()
    humedad = FloatField()
    lux = FloatField()
    fecha = DateTimeField()
    device_id = CharField()  # Add a new field for device ID

    class Meta:
        database = db

# Crear la tabla si no existe
db.connect()
db.create_tables([LecturaSensor], safe=True)
# Función para guardar la lectura del sensor en la base de datos
def guardar_lectura_sensor(device_id, temperatura, humedad, lux):
    # Verificar que todos los campos tengan valores válidos
    if temperatura is not None and humedad is not None and lux is not None:
        # Obtiene la fecha y hora actual
        fecha_actual = datetime.datetime.now()
        with db.atomic():
            LecturaSensor.create(
                temperatura=temperatura,
                humedad=humedad,
                lux=lux,
                fecha=fecha_actual,  # Asigna la fecha actual a la columna 'fecha'
                device_id=device_id
            )
    else:
        print("Advertencia: No se pudo guardar la lectura debido a valores nulos.")
        
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
            S.device_id = data.get('id')
            if S.device_id is None:
                # If "device_id" is missing, return an error response
                self.send_response(400)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write('Device ID not found in JSON data'.encode('utf-8'))
            else:
                # Now you can use the "device_id" to differentiate between devices
                if S.device_id == 'dispositivo1':
                    S.temperatura_device1 = float(data.get('temperatura')) if data.get('temperatura') is not None else None
                    S.humedad_device1 = data.get('humedad')
                    S.lux_device1 = data.get('lux')
                    print("Data received from Device 1:", data)
                    print('Temperature (Device 1):', S.temperatura_device1)
                    print('Humidity (Device 1):', S.humedad_device1)
                    print('Lux (Device 1):', S.lux_device1)
                    # Store the data in the database with the device ID
                    guardar_lectura_sensor(S.device_id, S.temperatura_device1, S.humedad_device1, S.lux_device1)

                elif S.device_id == 'dispositivo2':
                    S.temperatura_device2 = float(data.get('temperatura')) if data.get('temperatura') is not None else None
                    S.humedad_device2 = data.get('humedad')
                    S.lux_device2 = data.get('lux')
                    print("Data received from Device 2:", data)
                    print('Temperature (Device 2):', S.temperatura_device2)
                    print('Humidity (Device 2):', S.humedad_device2)
                    print('Lux (Device 2):', S.lux_device2)
                    
                    # Store the data in the database with the device ID
                    guardar_lectura_sensor(S.device_id, S.temperatura_device2, S.humedad_device2, S.lux_device2)

                # Create a JSON response for the MicroPython device
                data_to_micropython = {
                    "clave1_python": "valor1_python",
                    "clave2_python": "valor2_python"
                }
                response = json.dumps(data_to_micropython).encode('utf-8')

                # Configure the HTTP response
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(response)
        except json.JSONDecodeError as e:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(f'Error in the JSON received from MicroPython: {str(e)}'.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ("", port)  # esto hace correr el servidor en el ip local
    servidor = server_class(server_address, handler_class)
    print("Starting server....")
    servidor.serve_forever()

# Declarar temperatura_data como variable global
temperatura_data = [0]
bar_device1 = None
bar_device2 = None
canvas = None
ventana = None
# Función para crear y mostrar la interfaz gráfica
def crear_interfaz():
    global bar_device1, bar_device2, canvas, ventana  # Hacer que las variables sean globales

    #ventana = tk.Tk()
    
    # Create labels for Device 1 data
    etiqueta_temperatura_device1 = tk.Label(ventana, text="Device 1 - Temperatura:")
    etiqueta_humedad_device1 = tk.Label(ventana, text="Device 1 - Humedad:")
    etiqueta_lux_device1 = tk.Label(ventana, text="Device 1 - Lux:")

    # Create labels for Device 2 data
    etiqueta_temperatura_device2 = tk.Label(ventana, text="Device 2 - Temperatura:")
    etiqueta_humedad_device2 = tk.Label(ventana, text="Device 2 - Humedad:")
    etiqueta_lux_device2 = tk.Label(ventana, text="Device 2 - Lux:")

    # Create canvas for the bar chart for both devices
    canvas = tk.Canvas(ventana, width=400, height=200)
    canvas.pack()

    fig, ax = plt.subplots(figsize=(4, 2))
    bar_width = 0.35
    index = [0]
    bar_device1 = ax.bar(index, [0], bar_width, label='Device 1')
    bar_device2 = ax.bar([i + bar_width for i in index], [0], bar_width, label='Device 2')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(["Temperatura"])
    ax.set_ylim(0, 40)

    # Configure the canvas for the bar chart
    canvas = FigureCanvasTkAgg(fig, master=canvas)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    
    # Schedule a call to the update function
    ventana.after(1000, actualizar_grafico)

    # Position the labels in the window
    etiqueta_temperatura_device1.pack()
    etiqueta_humedad_device1.pack()
    etiqueta_lux_device1.pack()

    etiqueta_temperatura_device2.pack()
    etiqueta_humedad_device2.pack()
    etiqueta_lux_device2.pack()

    # Start the Tkinter main loop
    ventana.mainloop()
def actualizar_grafico():
        bar_device1[0].set_height(S.temperatura_device1)
        bar_device2[0].set_height(S.temperatura_device2)
        canvas.draw()   
# Función para actualizar las etiquetas y el gráfico con los valores de S
def actualizar_valores():
    global bar_device1, bar_device2
    # Access the data for both devices
    temperatura_device1 = S.temperatura_device1
    humedad_device1 = S.humedad_device1
    lux_device1 = S.lux_device1

    temperatura_device2 = S.temperatura_device2
    humedad_device2 = S.humedad_device2
    lux_device2 = S.lux_device2

    # Update the labels for Device 1 data
    etiqueta_temperatura_device1.config(text=f"Device 1 - Temperatura: {temperatura_device1}")
    etiqueta_humedad_device1.config(text=f"Device 1 - Humedad: {humedad_device1}")
    etiqueta_lux_device1.config(text=f"Device 1 - Lux: {lux_device1}")

    # Update the labels for Device 2 data
    etiqueta_temperatura_device2.config(text=f"Device 2 - Temperatura: {temperatura_device2}")
    etiqueta_humedad_device2.config(text=f"Device 2 - Humedad: {humedad_device2}")
    etiqueta_lux_device2.config(text=f"Device 2 - Lux: {lux_device2}")

    # Update the bar chart for both devices
    if bar_device1 is not None and bar_device2 is not None:
        bar_device1[0].set_height(S.temperatura_device1)
        bar_device2[0].set_height(S.temperatura_device2)
        canvas.draw()

    # Schedule a call to this function again after a time interval
    ventana.after(1000, actualizar_valores)


if __name__ == "__main__":
    # Configura las variables de instancia de la clase S
    S.device_id = None
    S.temperatura_device1 = None
    S.humedad_device1 = None
    S.lux_device1 = None
    S.temperatura_device2 = None
    S.humedad_device2 = None
    S.lux_device2 = None

    # Inicia el servidor en un subproceso (thread)
    server_thread = threading.Thread(target=run)
    server_thread.daemon = True
    server_thread.start()
    
    # Inicia la interfaz gráfica en un hilo separado (thread)
    interfaz_thread = threading.Thread(target=crear_interfaz)
    interfaz_thread.start()
    
    # Crear y configurar la ventana principal de la interfaz gráfica
    ventana = tk.Tk()
    ventana.title("Lecturas de Sensores")

    # Crear y posicionar las etiquetas para los valores de los dispositivos
    etiqueta_temperatura_device1 = tk.Label(ventana, text="Device 1 - Temperatura:")
    etiqueta_humedad_device1 = tk.Label(ventana, text="Device 1 - Humedad:")
    etiqueta_lux_device1 = tk.Label(ventana, text="Device 1 - Lux:")

    etiqueta_temperatura_device2 = tk.Label(ventana, text="Device 2 - Temperatura:")
    etiqueta_humedad_device2 = tk.Label(ventana, text="Device 2 - Humedad:")
    etiqueta_lux_device2 = tk.Label(ventana, text="Device 2 - Lux:")

    etiqueta_temperatura_device1.pack()
    etiqueta_humedad_device1.pack()
    etiqueta_lux_device1.pack()

    etiqueta_temperatura_device2.pack()
    etiqueta_humedad_device2.pack()
    etiqueta_lux_device2.pack()

    # Crear y configurar el lienzo para el gráfico de barras
    canvas = tk.Canvas(ventana, width=400, height=200)
    canvas.pack()

    fig, ax = plt.subplots(figsize=(4, 2))
    bar_width = 0.35
    index = [0]
    bar_device1 = ax.bar(index, [0], bar_width, label='Device 1')
    bar_device2 = ax.bar([i + bar_width for i in index], [0], bar_width, label='Device 2')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(["Temperatura"])
    ax.set_ylim(0, 40)

    canvas = FigureCanvasTkAgg(fig, master=canvas)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Función para actualizar el gráfico y los valores de los dispositivos
    def actualizar_datos_y_grafico():
        actualizar_valores()  # Actualiza los valores de los dispositivos
        actualizar_grafico()  # Actualiza el gráfico

    # Programar una llamada periódica para actualizar los datos y el gráfico
    ventana.after(1000, actualizar_datos_y_grafico)

    # Iniciar el bucle principal de Tkinter
    ventana.mainloop()
    