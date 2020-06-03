import socketserver
import json
from signal import pause
from threading import Thread
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

PORT = 3000
IP = "127.0.0.1"
TOKEN = "S8RL9Z6Y22TYQK45JB4V8PHRJJMD9DS9"


class GSIServer(ThreadingHTTPServer):
    def __init__(self, post_callback=None):
        self.post_callback = post_callback
        super().__init__((IP, PORT), GSIHandler)


class GSIHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server: GSIServer):
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.send_response(405)
        self.send_header("content-type", "application/json")
        self.end_headers()

        self.wfile.write(
            bytes(json.dumps({"error": "Method not allowed", "code": 405}), "ascii"))

    def do_POST(self):
        data = json.load(self.rfile)
        if TOKEN != data["auth"]["token"]:
            print("Request NOT authorized")
        elif self.server.post_callback:
            self.server.post_callback(data)

        self.send_response(200)
        self.end_headers()



class GSIConnection(Thread):
    """
    An object for starting and handling the required events and the http server for game state integration.
    """
    def __init__(self):
        self.server = GSIServer(post_callback=self.handle_post)
        self.listeners = []
        super().__init__(daemon=True)

    def run(self):
        self.server.serve_forever()

    def block(self):
        pause()

    def handle_post(self, data):
        for func in self.listeners:
            func(data)

    def add_post_listener(self, func):
        self.listeners.append(func)

    def on_post(self, func):
        """
        Decorator for on_post events
        ```
        connection = GSIConnection()

        @connection.on_post
        def handle_post(data):
            print(data)
        ```
        """
        self.add_post_listener(func)

        def wrap(x):
            func(x)
        return wrap


class CSGOConnection(GSIConnection):
    pass
