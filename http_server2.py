#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import socket
import time
UDP_IP = "fd12:3456::5232:5fff:fe42:8a37"
UDP_IP1 = "fd12:3456::b6e3:f9ff:fea6:2e7"

UDP_PORT = 5001
HOST_IP="fd12:3456::1"
PORT = 5005
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        received_data = json.loads (post_data)
        try:
            con_data=received_data["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"]
            print(con_data)
            MESSAGE=con_data
            print ("message:", MESSAGE) 

            message_bytes = str.encode(MESSAGE) 
            sock = socket.socket(socket.AF_INET6, # Internet
                            socket.SOCK_DGRAM) # UDP
            sock.sendto(message_bytes, (UDP_IP, UDP_PORT))
            sock.sendto(message_bytes, (UDP_IP1, UDP_PORT))
            time.sleep(1)
            sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            sock.bind((HOST_IP, PORT))
            print(f"Listening to {HOST_IP}/{PORT} for incoming messages")
            
            data, addr = sock.recvfrom(2048) # buffer size is 2048 bytes
            print ("received message:", data)
            

        except:
            
           # logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                #str(self.path), str(self.headers), post_data.decode('utf-8'))

            self._set_response()
            self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=1400):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()




