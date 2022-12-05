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
        if sentence in ['help', '도움말']:
            return_message = crawling.help()
        elif sentence in ['notice', '공지', '학사공지']:
            return_message = crawling.campusNotice()
        elif sentence in ['news', '뉴스']:
            return_message = crawling.news()
        elif sentence in ['music', 'musicrank', 'musicranking', '뮤직', '음악']:
            return_message = crawling.musicRanking()
        elif sentence in ['movie', 'movierank', 'movieranking','영화','영화순위']:
            return_message = crawling.movieRanking()
        elif sentence.startswith('stock') or sentence.startswith('주식'):
            return_message = crawling.stockPrice(sentence.strip('stock: ''주식: '))
        elif sentence in ['weather', '날씨']:
            return_message = crawling.weather()
        
        else:
            return_message = 'Undefined command, type "help" to see commands'

        connectionSocket.send(return_message.encode())
    connectionSocket.close()
    
    

# connectionSocket.close()
    

