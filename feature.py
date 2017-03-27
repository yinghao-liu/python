#!/usr/bin/python
# generate https.pem with following command:
# openssl req -new -x509 -keyout https.pem -out https.pem -days 3650 -nodes
# 


import BaseHTTPServer
import SimpleHTTPServer
import thread
import ssl
import sys

HTTPS_PORT = 443
HTTP_PORT  = 8000


class RequestHandle(BaseHTTPServer.BaseHTTPRequestHandler):
	Page = """\
		<html>
			<body>
				<p>this is https server</p>
			</body>
		</html>
		"""
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-Type","text/html")
		self.send_header("Content-Length",str(len(self.Page)))
		self.end_headers()
		self.wfile.write(self.Page)

def https_server(PORT):
	server=BaseHTTPServer.HTTPServer(('0.0.0.0',PORT),RequestHandle)
	server.socket=ssl.wrap_socket(server.socket, certfile='./https.pem', server_side=True)
	server.serve_forever()


def http_server(PORT):
	#server=BaseHTTPServer.HTTPServer(('0.0.0.0',PORT),SimpleHTTPServer.SimpleHTTPRequestHandler)
	server=BaseHTTPServer.HTTPServer(('0.0.0.0',PORT),RequestHandle)
	server.serve_forever()

def main():
	#thread.start_new_thread(https_server, (HTTPS_PORT,))
	thread.start_new_thread(http_server, (HTTP_PORT,))
	while True:
		pass

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print "you kill me!"
		sys.exit()
	except SSLError:
		pass
