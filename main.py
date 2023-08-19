# -*-coding: utf-8 -*-
#服务端
#引入socket库
import socket
#这是进行定义一个ip协议版本AF_INET（IPv4），定义一个传输TCP协议，SOCK_STREAM
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#定义ip地址与端口号，ip地址就是服务端的ip地址，端口随便定义，但要与客户端脚本一致
ip_port=("127.0.0.1",8000)
#绑定一个端口
sk.bind(ip_port)
#监听一个端口,这里的数字3是一个常量，表示阻塞3个连接，也就是最大等待数为3
sk.listen(3)

#客户端发送的数据存储在recv里，1024指最大接受数据的量

#接受客户端的数据，并返回两个参数，a为连接信息，b为客户端的ip地址与端口号

while True:
    a,b=sk.accept()
    data=a.recv(1024)
    print(data.decode('utf-8'))
    print(a)
    message='''200 \
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: </p>
        <p>Message: </p>
        <p>Error code explanation:</p>
    </body>
</html>'''
    a.send(message.encode('utf-8'))
    if message==('bye'):
        break