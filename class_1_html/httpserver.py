import sys
import http.server
from http.server import SimpleHTTPRequestHandler
import socket
import os

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = http.server.HTTPServer
Protocol     = "HTTP/1.0"

server_address = ('0.0.0.0', 8000)

os.chdir(os.path.dirname(__file__))

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
print(ip)
s.close()
httpd.serve_forever()