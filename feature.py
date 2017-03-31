#!/usr/bin/python
import BaseHTTPServer

class RequestHandle(BaseHTTPServer.BaseHTTPRequestHandler):
	Page = """\
		<html>
			<body>
				<p>hello,web!</p>
			</body>
		</html>
		"""
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-Type","text/html")
		self.send_header("Content-Length",str(len(self.Page)))
		self.end_headers()
		#self.wfile.write(self.Page)
		self.wfile = self.Page

server=BaseHTTPServer.HTTPServer(('0.0.0.0',8000),RequestHandle)
server.serve_forever()


