from socket import *
serverName = '100.97.38.60'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('100.97.38.60', 5432))
message = input('Input a lower case sentence : ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
clientSocket.close()
print ("UDP client completed - exiting")
