from socket import * 
serverPort = 12000 
messageNumber = 1

serverSocket = socket(AF_INET,SOCK_STREAM) 

serverSocket.bind(('',serverPort)) 
serverSocket.listen(2) 
print ('The server waiting to receive two connections...') 
connectionSocket, addr = serverSocket.accept() 
print('Accepted first connection, calling it client X') 
connectionSocket2, addr = serverSocket.accept()
print('Accepted second connection, calling it client Y')  
connectionSocket.send(b'From Server: Client X Connected') 
connectionSocket2.send(b'From Server: Client Y Connected')

print('Waiting to receive messages from client X and client Y...')   
while messageNumber < 3:
  messageOne = connectionSocket.recv(1024).decode()
  messageTwo = connectionSocket2.recv(1024).decode()
  if messageNumber == 1:
    print('Client X sent message 1:', messageOne)        
    messageNumber += 1
    connectionSocket.close()  
  if messageNumber == 2:
    print('Client Y sent message 2:', messageTwo)  
    messageNumber += 1
    connectionSocket2.close() 
serverSocket.close()