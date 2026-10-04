#!/usr/bin/env python3
"""Serve the viva guide for local reading.

    python3 preview_server.py [port]      # default 8080, binds 0.0.0.0

`/` serves the multi-page site (MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE/);
the single-file version stays reachable at
/MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE.html. Search + accordions need a
real browser.
"""
import http.server
import os
import socketserver
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SITE_INDEX = "/MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE/index.html"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def do_GET(self):
        if self.path in ("/", ""):
            self.path = SITE_INDEX
        return super().do_GET()

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print("Viva guide on http://0.0.0.0:%d/  (site: %s)" % (PORT, os.path.join(ROOT, SITE_INDEX.lstrip('/'))))
        httpd.serve_forever()
