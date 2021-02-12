import socket  # 网络通信 TCP，UDP

mystr = "1_lbt4_10#32899#002481627512#0#0#0:1289671407:你的baby:你的hello:288:你好妹子"

# socket.AF_INET  网络通信，Windows AF_INET
# socket.SOCK_DGRAM报文
for i in range(256):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.connect(("10.10.153." + str(255 - i), 2425))
    udp.send(mystr.encode("gbk"))
    print(i)
