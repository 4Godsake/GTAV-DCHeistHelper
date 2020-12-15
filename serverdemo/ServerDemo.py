import time
import threading
import queue
import socket


# 三个线程：
# 线程1：产生递增的数字，转成字符串放到队列中
# 线程2：监听端口，将产生的连接放到列表中
# 线程3：从队列中取出数字，遍历连接列表，发送到所有客户端

# 线程1：产生递增的数字，转成字符串放到队列中
class Producer(threading.Thread):

    def __init__(self, work_queue):
        super().__init__()  # 必须调用
        self.work_queue = work_queue

    def run(self):
        # print("Begin produce...")
        num = 1
        while True:
            self.work_queue.put(str(num))
            num = num + 1
            time.sleep(1)  # 暂停1秒


# 线程2：监听端口，将产生的连接放到列表中
class SocketServer(threading.Thread):

    def __init__(self, socket_list, kill_flag):
        super().__init__()
        self.socket_list = socket_list
        self.kill_flag = kill_flag

    def run(self):
        sock = socket.socket()
        sock.bind(('127.0.0.1', 9092))
        sock.listen(5)
        print("Start listen...")
        while True:
            conn, addr = sock.accept()
            print("Connect by", addr)
            self.socket_list.append((conn, addr))
            # msg = conn.recv(1024)
            # print("msg received:", msg.decode('utf-8'))
            # if msg.decode('utf-8') == "hi":
            #     self.kill_flag.put(True)
            #     print("收到hi，更改flag为true")



# 线程3：从队列中取出数字，遍历连接列表，发送到所有客户端
class Printer(threading.Thread):

    def __init__(self, work_queue, socket_list, kill_flag):
        super().__init__()  # 必须调用
        self.work_queue = work_queue
        self.socket_list = socket_list
        self.kill_flag = kill_flag

    def run(self):
        while True:
            num = self.work_queue.get()  # 当队列为空时，会阻塞，直到有数据
            for conn, addr in self.socket_list:  # 遍历保存连接的列表
                print("Send", num, "To", addr)
                # if self.kill_flag.get():
                try:
                    conn.sendall(bytes(num + '\r\n', 'utf-8'))  # 把字符串转换成字节数组发送
                except:
                    print("Disconnect by", addr)  # 如果连接断开，发送会失败
                    self.socket_list.remove((conn, addr))  # 从列表中删除断开的连接
                    conn.sendall(bytes('someone disconnected', 'utf-8'))
                # else:
                # conn.sendall(bytes('someone send something', 'utf-8'))



def main():
    kill_flag = queue.Queue()
    work_queue = queue.Queue()
    socket_list = []  # 为了更安全可靠，从多线程访问列表时应该加锁，
    # 这里做了简化，因为列表的增加删除操作基本上可以认为是线程安全的

    socket_server = SocketServer(socket_list, kill_flag)
    socket_server.daemon = True
    socket_server.start()

    printer = Printer(work_queue, socket_list, kill_flag)
    printer.daemon = True  # 当主线程退出时子线程也退出
    printer.start()

    producer = Producer(work_queue)
    producer.daemon = True  # 当主线程退出时子线程也退出
    producer.start()

    time.sleep(1)  # 这里要暂停一下，否则执行下一条语句时，会因队列为空而直接返回
    work_queue.join()  # 主线程会停在这里，直到所有数字被get()，并且task_done()，因为没有调用task_done()，所在这里会一直阻塞，直到用户按^C


if __name__ == '__main__':
    main()
