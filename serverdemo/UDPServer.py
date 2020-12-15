import socketserver
from typing import Any

global client_list
client_list = []


class MyRequestHanlde(socketserver.BaseRequestHandler):

    # def __init__(self, request: Any, client_address: Any, server: socketserver.BaseServer):
    #     super().__init__(request, client_address, server)
    #     global client_list
    #     client_list = []
    #     self.client_list = self.client_list

    def handle(self):
        global client_list
        client_data = self.request[0]
        server = self.request[1]
        client_address = self.client_address
        client_list.append(client_address)
        for addr in client_list:
            print(addr)
            try:
                server.sendto(bytes('这是一条广播', 'utf-8'), addr)
            except:
                print("Disconnect by", addr)  # 如果连接断开，发送会失败
                client_list.remove(addr)  # 从列表中删除断开的连接

        print(self.request)
        print("客户端发来的数据%s" % client_data)
        server.sendto(client_data.upper(), client_address)
        # self.server.


def main():
    s = socketserver.ThreadingUDPServer(('127.0.0.1', 9092), MyRequestHanlde)
    s.serve_forever()


if __name__ == '__main__':
    main()
