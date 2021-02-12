import socket
import time
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8848))
server.listen(5)

clientSock, clientAddr = server.accept()

while True:
    data = clientSock.recv(1024)
    print(data.decode("UTF-8"))
    # os.system(data.decode("UTF-8"))
    sendData = (data.decode("UTF-8") + ' ' + str(time.time())).encode("UTF-8")
    clientSock.send(sendData)

clientSock.close()
server.close()
