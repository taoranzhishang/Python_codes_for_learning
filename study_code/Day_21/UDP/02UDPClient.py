import socket  # 网络通信UDP TCP

udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Entry:")
    udpClient.sendto(message.encode("UTF-8"), ("127.0.0.1", 8848))  # 发消息
    print(udpClient.recv(1024).decode("UTF-8"))  # 收消息

udpClient.close()
