import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    # msg = input('>>>:').strip()
    # client.sendto(msg.encode('utf-8'), ('127.0.0.1', 9092))
    host = "127.0.0.1"
    # 设置端口
    port = 9092
    # 连接服务端
    client.connect((host, port))
    res = client.recvfrom(1024)
    print(res)
client.close()
