# -*-coding: utf-8 -*-
#服务端
#引入socket库
import socket
import time
import os
import re

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

def get_dir(path):
    for item in os.walk(path):
        return item[1]
    
def get_dir_num(path):
    for item in os.walk(path):
        return len(item[1])

def get_link(path):
    for item in os.walk(path):
        return item[0]
    
def produce(name,link):
    main="<tr><td class='name'>"+name+"</td><td class='size'>"+link+"</td>"+"<td class='more'>123</td></tr>"
    return main

def merge_catalog(path):
    main=""
    for i in range(0,get_dir_num(path),1):
        print(produce(get_dir(path)[i],get_link(path)))
        main+=produce(get_dir(path)[i],get_link(path))+"\n"
    return main
one=merge_catalog("./")

while True:
    a,b=sk.accept()
    data=a.recv(1024)
    print(data.decode('utf-8'))
    print(a)
    message='''HTTP/1.0 200 OK
Content-Type: text/html

<html>
    <head>
        <meta charset="utf-8">
        <title>服务器文件</title>
    </head>
    <body>
        <h1>服务器文件管理系统</h1>
        <table class="table_file" border="1" cellspacing="0">
            <tr>
            <th >名字</th>
            <th >大小</th>
            <th >操作</th>
            </tr>
            <tr>
            <td class="name">123</td>
            <td class="size">123</td>
            <td class="more">123</td>
            </tr>'''+one+'''
        </table>
    </body>
    <style>
    .table_file{
    width:800px;
    }
    .table_file td {
    text-align: center;
    }
</style>
</html>'''
    # time.sleep(1)
    a.send(message.encode('utf-8'))
    
    break





