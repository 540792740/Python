#找到目录下有hello.py的文件
import os


file_list = []
def find_hello(parent_dir, file_name):
    file_abspath = os.path.join(parent_dir, file_name)
    if os.path.isdir(file_abspath):
        for f in os.listdir(file_abspath):
            # print(file_abspath)
            find_hello(file_abspath, f)
    else:
        if file_abspath.endswith(".py"):    #获得当前目录列表
            if read_and_find_hello(file_abspath):
                print(file_abspath)
                file_list.append(file_name)


def read_and_find_hello(py_file):
    f = open(py_file, encoding="utf8")

    flag = False
    while True:
        # line = [line.decode('utf-8') for line in f.readlines()]
        line = f.readline()
        if line == "":
            break
        elif "print" in line:
            flag = True
            break
    f.close()
    return flag


find_hello("E:\Stevens Institute of Technology\CPE-551-Python\Project","Python3Pakage")
# read_and_find_hello("E:\Stevens Institute of Technology\CPE-551-Python\Project/Python3Pakage/11.1LambdaFuc.py")
print(file_list)
