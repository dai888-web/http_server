import socket
import re
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=("127.0.0.1",80)
sk.bind(ip_port)
sk.listen(3)
def findall(data):
    print(data)
    if(data[0:3]==r"GET"):
        print("11")
        kk=re.compile(r"^GET /\S*")
        data=re.findall(kk,data)
        return data[0][5:]


while True:
    message=""
    a,b=sk.accept()
    print("成功")
    data=a.recv(1024)
    option=findall(data.decode('utf-8'))
    if (option==""):
        f = open("index.html")
        lines = f.read()
        f.close()
        message="HTTP/1.0 200 OK\nContent-Type: text/html\n\n"+lines
        a.send(message.encode("utf-8"))
    if(option=="favicon.ico"):
        f = open("favicon.ico",'rb')
        lines = f.read()
        f.close()
        message="HTTP/1.0 200 OK\nContent-Type: image/x-icon\n\n"
        a.send(message.encode("utf-8")+lines)
        
    print("线程结束")
    a.close()


