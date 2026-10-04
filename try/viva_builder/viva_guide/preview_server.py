#!/usr/bin/env python3
"""Serve the viva guide at / for local reading (search + accordions need a real browser).

    python3 preview_server.py [port]      # default 8080, binds 0.0.0.0
"""
import http.server
import os
import socketserver
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.abspath(os.path.join(HERE, "..", "..", "..", "MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE.html"))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=os.path.dirname(GUIDE), **kw)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            payload = open(GUIDE, "rb").read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        return super().do_GET()

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print("Viva guide on http://0.0.0.0:%d/  (%s)" % (PORT, GUIDE))
        httpd.serve_forever()
