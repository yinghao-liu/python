#!/usr/bin/env python3
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
HTTP_PORT  = 8000

class RequestHandle(BaseHTTPRequestHandler):
	Page = """\
		<html>
		<body>
		<p>this is http server</p>
		</body>
		</html>
		"""
	def do_GET(self):
		print(type(self.wfile))
		print(type(self.rfile))
		self.send_response(200)
		self.send_header("Content-Type","text/html")
		self.send_header("Content-Length",str(len(self.Page)))
		self.end_headers()
		self.wfile.write(bytes(self.Page, encoding="utf8"))
	

	def do_POST(self):
		leng=self.headers["Content-Length"]
		print(self.rfile.read(int(leng)))
		self.send_response(200)
		self.send_header("Content-Type","text/html")
		self.send_header("Content-Length",str(len(self.Page)))
		self.end_headers()
		self.wfile.write(bytes(self.Page, encoding="utf8"))

def http_server(PORT):
	server=HTTPServer(('0.0.0.0', PORT), RequestHandle)
	server.serve_forever()

if "__main__" == __name__:
	http_server(HTTP_PORT)
