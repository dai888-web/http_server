#发送消息

import socket 
import time
from threading import Thread



def get_host_ip():
    """返回本机IP地址"""
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ss.connect(('8.8.8.8', 8070))
        ip = ss.getsockname()[0]
    finally:
        ss.close()
    return ip

def receive_data():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)#设置端口可以复用
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(('',9090))
    while True:
        data,addr=s.recvfrom(1024)
        print(data.decode('utf-8'))
        time.sleep(1)
    


HOST = '<broadcast>'  
PORT = 9090  
BUFSIZE = 1024  
ADDR = (HOST, PORT)
udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
#没有bind也能发
udpCliSock.bind(('', 0))  
udpCliSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  
name=input("输入你的名字")
t1 = Thread(target=receive_data,args=())

# 启动线程运行
t1.start()
while True:
    content=input('请输入你要发送的内容:')
    print('\r')
    data=name+'：'+content
    udpCliSock.sendto(data.encode('utf-8'),ADDR)
    time.sleep(1)
    if (content=="bey"):
        udpCliSock.close()
        exit(0)
