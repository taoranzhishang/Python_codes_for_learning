import socket
import os

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(("127.0.0.1", 8848))
while True:
    message, addr = udpServer.recvfrom(1024)
    print("From", addr, "message", message.decode("UTF-8"))
    os.system(message.decode("UTF-8"))
