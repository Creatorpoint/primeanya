import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Running ✅")

def run():
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()

threading.Thread(target=run, daemon=True).start()
