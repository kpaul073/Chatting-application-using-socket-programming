from socket import *
import crawling


serverPort = 12000
serverSocket= socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)
print ("The server is now ready to receive")

while True:
    connectionSocket, address = serverSocket.accept()
    sentence = connectionSocket.recv(2048).decode()

    if sentence == 'quit':
        return_message = 'Disconnection from server side'
        connectionSocket.send(return_message.encode())
        

    else:
        if sentence in ['notice']:
            return_message = crawling.campusNotice()
        else:
            return_message = 'Undefined command, type "help" to see commands'

        connectionSocket.send(return_message.encode())
    connectionSocket.close()
    
    

# connectionSocket.close()
    

