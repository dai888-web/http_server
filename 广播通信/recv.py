#接收消息

import socket
import time
#初始化udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)#设置端口可以复用
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',9090))
while True:
    data,addr=s.recvfrom(1024)
    print(data.decode('utf-8'))
    time.sleep(1)
s.close()
exit(0)