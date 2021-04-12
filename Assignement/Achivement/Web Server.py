from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM) 

serverPort = 80
serverSocket.bind(('172.19.116.131',serverPort))
serverSocket.listen(1)#only one client can connect to the web server

while True:

	print ('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	print ("addr:\n")
	try:
		message = connectionSocket.recv(1024)
		print ("message: \n")
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read() 
		print ("outputdata:")
		first_header = "HTTP/1.1 200 OK"
		header_info = {
			"Content-Length": len(outputdata),
			"Keep-Alive": "timeout=%d,max=%d" %(10,100),
			"Connection": "Keep-Alive",
			"Content-Type": "text/html"
		}
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.close()
	except IOError:
		connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
		connectionSocket.close()
serverSocket.close()
sys.close()
