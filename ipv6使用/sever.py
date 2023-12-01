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


def findall(data):
    print(data)
    if (data[0:3] == r"GET"):
        kk = re.compile(r"^GET /\S*")
        data = re.findall(kk, data)
        return data[0][5:]


while True:
    message = ""
    item = []
    print("成功")
    a, b = sk.accept()
    data = a.recv(1024)
    option = findall(data.decode('utf-8'))
    print(option)
    if option == None:
        continue
    if (option == ""):
        f = open("src/index.html", 'rb')
        lines = f.read()
        f.close()
        message = "HTTP/1.0 200 OK\nContent-Type: text/html\n\n"
        a.send(message.encode("utf-8")+lines)
    elif (option[-3:] == "ico" or option[-4:] == "ICO"):
        f = open("src/"+option, 'rb')
        lines = f.read()
        f.close()
        message = "HTTP/1.0 200 OK\nContent-Type: image/x-icon\n\n"
        a.send(message.encode("utf-8")+lines)
    elif (option[-4:] == "html" or option[-4:] == "HTML"):
        f = open(option, 'rb')
        lines = f.read()
        f.close()
        message = "HTTP/1.0 200 OK\nContent-Type: text/html\n\n"
        a.send(message.encode("utf-8")+lines)
    elif (option[-3:] == "jpg" or option[-3:] == "png" or option[-3:] == "bmp"):
        f = open(option, 'rb')
        lines = f.read()
        f.close()
        message = "HTTP/1.0 200 OK\nContent-Type: image\n\n"
        a.send(message.encode("utf-8")+lines)
    a.close()
