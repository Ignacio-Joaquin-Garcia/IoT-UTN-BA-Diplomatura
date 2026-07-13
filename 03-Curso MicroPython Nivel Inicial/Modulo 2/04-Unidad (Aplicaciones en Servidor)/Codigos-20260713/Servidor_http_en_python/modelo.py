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
            # Decodificar el JSON recibido
            data = json.loads(post_data.decode('utf-8'))
            print("Datos recibidos:", data)
            self.send_response(200)
            self.end_headers()
            response_text = 'Solicitud POST recibida con éxito'
            self.wfile.write(response_text.encode('utf-8'))
            
        except json.JSONDecodeError as e:
            print('no logrado')
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f'Error en el JSON recibido: {str(e)}'.encode('utf-8'))


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
