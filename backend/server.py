from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthy":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Healthy")
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
