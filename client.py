from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = clientSocket.recv(1024)
print(message.decode())
sentence = input('Enter message to send to server:')
clientSocket.send(sentence.encode())
clientSocket.close()