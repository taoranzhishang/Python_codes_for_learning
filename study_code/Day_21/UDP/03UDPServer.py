import socket
import time

udpBackdoor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpBackdoor.bind(("127.0.0.1", 8848))  # 绑定端口，接收该端口的消息
while True:
    message, addr = udpBackdoor.recvfrom(1024)  # 1024 缓冲区
    print("From", addr, "message", message.decode("UTF-8"))
    sendData = ((message.decode("UTF-8") + ' ' + str(time.time())).encode("UTF-8"))
    udpBackdoor.sendto(sendData, addr)  # 发送数据到指定地址
