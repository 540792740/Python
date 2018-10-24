import os

for info in os.listdir(r'E:\Stevens Institute of Technology\CPE-551-Python\Project/Python3Pakage'):
    print(info)
    a = os.path.abspath(r'E:\Stevens Institute of Technology\CPE-551-Python\Project/Python3Pakage') #获取文件夹的路径，此处其实没必要这么写，目的是为了熟悉os的文件夹操作
    info = os.path.join(a,info) #将路径与文件名结合起来就是每个文件的完整路径
    info = open(info,'r') #读取文件内容
    # print(info.readline()) #使用readline函数得到一条一条的信息，如果使用read获取全部信息亦可；
    # info.close()