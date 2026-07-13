from http.server import BaseHTTPRequestHandler, HTTPServer
import json


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
            temperatura = float(data.get('temperatura')) if data.get('temperatura') is not None else None
            humedad = data.get('humedad')
            lux = data.get('lux')
            print("Datos recibidos desde MicroPython:", data)
            print('temperatura: ' + str(temperatura))
            print('humedad: ' + str(humedad))
            print('lux: ' + str(lux))
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


if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
