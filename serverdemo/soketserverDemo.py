import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print(self.request, self.client_address, self.server)
        conn = self.request
        # conn.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', 'utf-8'))
        flag = True
        while flag:
            data = conn.recv(1024).decode("utf-8")
            print('收到：', data)
            if data == "exit":
                flag = False
                self.server.shutdown()
            elif data == "0":
                conn.sendall(bytes('通过可能会被录音.balabala一大推', 'utf-8'))
            else:
                conn.sendall(bytes('请重新输入.', 'utf-8'))


if __name__ == '__main__':
    server = socketserver.ThreadingUDPServer(('127.0.0.1', 9092), MyServer)
    server.serve_forever()
