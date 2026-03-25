import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Prime Analytics Bot Running ✅</h1>")

def run():
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()

threading.Thread(target=run, daemon=True).start()
