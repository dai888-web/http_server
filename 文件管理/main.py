import os
from os import walk


def get_file(str):
    return os.popen('tree '+str).read()


if __name__ == "__main__":

    

# folder path
    dir_path = r'F:\\outline\\http_server'

# list to store files name
    res = []
    i=0
    for (dir_path, dir_names, file_names) in walk(dir_path):
        res.extend(file_names)
        if i==3:
            break
    i+=1
    print(res)
# for filename in os.listdir():
#     print(filename)
