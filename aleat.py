#!/usr/bin/python
# Borja Egea Madrid

import socket

class webApp:

	 def parse(self, request):
		  return None

	 def process(self, parsedRequest):
		  return ("200 OK", "<html><body><h1>It works!</h1></body></html>")

	 def __init__(self, hostname, port):

		  # Create a TCP objet socket and bind it to a port
		  mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		  mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		  mySocket.bind((hostname, port))
	
		  # Queue a maximum of 5 TCP connection requests
		  mySocket.listen(5)
	
		  # Accept connections, read incoming data, and call
		  # parse and process methods (in a loop)

		  while True:
			   print 'Waiting for connections'
			   (recvSocket, address) = mySocket.accept()
			   print 'HTTP request received (going to parse and process):'
			   request = recvSocket.recv(2048)
			   print request
			   parsedRequest = self.parse(request)
			   (returnCode, htmlAnswer) = self.process(parsedRequest)
			   print 'Answering back...'
			   recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
					                  + htmlAnswer + "\r\n")
			   recvSocket.close()
	
class aleatApp(webApp):
	
	 def process(self, parsedRequest):
		  import random
		  respuesta = '<a href = "' + str(random.randint(1,1000000)) + '">Dame otra</a>'
		  return ("200 OK", "<html><body><h1>" + respuesta + "<h1><body><html>")

if __name__ == "__main__":
	testWebApp = aleatApp("localhost", 1234)
	
