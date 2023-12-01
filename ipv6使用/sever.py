import socket
import re

# 创建套接字
sk = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# 设置IP和端口
host = ''
port = 80
# bind绑定该端口
sk.bind((host, port))
# 监听
sk.listen(10)
a,b=sk.accept()
data=a.recv(1024)
data.decode('utf-8')

