import socket
import threading

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=("127.0.0.1",8005)
sk.bind(ip_port)
sk.listen(3)

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):              #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        pass
        data=a.recv(1024)
        print(data)
        f = open("index.html")
        lines = f.read()
        f.close()
        message="HTTP/1.0 200 OK\nContent-Type: text/html\n\n"+lines
        a.send(message.encode("utf-8"))
        print("线程结束")


while True:
    a,b=sk.accept()
    print("成功")
    thread1 = myThread(1, "Thread-1", 1)
    thread1.start()
a.close()

    # data=a.recv(1024)
    # print(data)
    # a.send("123456".encode('utf-8'))
    # a.close()




