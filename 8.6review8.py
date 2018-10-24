names = [11, 22, 33, 44]
names2= ('aa', 'bb', 'cc', 'dd')
j = 0
i = 0
print("number \t content")      #\t是tab键，一个制表符
for i in names:
    for j in names2:
        print("%d \t %s"%(i,j))
        break
    i = i + 1
# 枚举法
for i,item in enumerate(names2,4): #从4开始计数
    print("%d \t %s"%(i,item))