import socket
import re
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=("127.0.0.1",8003)
sk.bind(ip_port)
sk.listen(3)
def findall(data):
    print(data)
    if(data[0:3]==r"GET"):
        kk=re.compile(r"^GET /\S*")
        data=re.findall(kk,data)
        return data[0][5:]
while True:
    message=""
    item=[]
    print("成功")
    a,b=sk.accept()
    data=a.recv(1024)
    option=findall(data.decode('utf-8'))
    if option==None:
        continue
    if (option==""):
        f = open("index.html",'rb')
        lines = f.read()
        f.close()
        message="HTTP/1.0 200 OK\nContent-Type: text/html\n\n"
        a.send(message.encode("utf-8")+lines)
    elif (option[-3:]=="ico" or option[-4:]=="ICO"):
        f = open(option,'rb')
        lines = f.read()
        f.close()
        message="HTTP/1.0 200 OK\nContent-Type: image/x-icon\n\n"
        a.send(message.encode("utf-8")+lines)
    elif (option[-4:]=="html" or option[-4:]=="HTML"):
        f = open(option,'rb')
        lines = f.read()
        f.close()
        message="HTTP/1.0 200 OK\nContent-Type: text/html\n\n"
        a.send(message.encode("utf-8")+lines)
    a.close()