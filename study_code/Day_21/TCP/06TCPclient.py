import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8848))

while True:
    message = input("Entry:")
    client.send(message.encode("UTF-8"))
    data = client.recv(1024)
    print(data.decode("UTF-8"))

client.close()
