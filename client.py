from socket import *

serverName= '192.168.0.10'
serverPort= 12000

while True:
    clientSocket= socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    sentence = input('>>')
    if sentence == 'quit':
        print('Closing the Server')
        clientSocket.send(sentence.encode())
        clientSocket.close()
        break
        
    else:
        clientSocket.send(sentence.encode())
        modifiedSentence= clientSocket.recv(1024)
        print (modifiedSentence.decode())

