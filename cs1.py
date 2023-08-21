import re
data="GET /123/5135131/2313/54135 HTTP/1.1 Host: 127.0.0.1:8006"
def findall(data):
    print(data)
    if(data[0:3]==r"GET"):
        kk=re.compile(r"^GET /\S*")
        data=re.findall(kk,data)
        return data[0][5:]

def split_path(data):
    data=findall(data)+" "
    kk=re.compile(r"[^/]* $")
    data=re.findall(kk,data)
    print(data)

split_path(data)