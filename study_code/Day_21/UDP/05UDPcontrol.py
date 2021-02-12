import socket

udpControl = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input("Entry:")
    udpControl.sendto(message.encode("UTF-8"), ("127.0.0.1", 8848))

udpControl.close()
