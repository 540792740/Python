import os


file_list = []
def find_hello(file_abspath):
    for f in os.listdir(file_abspath):
        # print(f)
        if f.endswith(".py"):    #获得当前目录列表
            a = os.path.abspath(f)
            if read_and_find_hello(f):
                # print(f)
                file_list.append(f)


def read_and_find_hello(py_file):
    f_open = open(py_file, encoding="utf8")
    flag = False
    # print(py_file)
    while True:
        line = f_open.readline()
        if line == '':
            break
        elif "hello" in line:
            flag = True
            break
    f_open.close()
    return flag

find_hello("E:/Stevens Institute of Technology/CPE-551-Python/Project/Python3Pakage")

print(file_list)

