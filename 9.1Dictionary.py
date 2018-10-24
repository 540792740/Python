stu = {"name":"JW","guaiguai":"Cute"}
for i in stu.keys():
    print(i)
for k in stu.values():
    print(k)
print("=" * 30)
# 迭代字典的常用方式
for item in stu.items():
    print("key is %s, value is %s"%item)

print('='*30)
print('Student Management System'.center(50))
print('input 1: Add a Student Name'.center(50))
print('input 2: Find a Student Name'.center(50))
print('input 3: Change a Student Name'.center(50))
print('input 4: Remove a Student Name'.center(50))
print('input 5: Display all Students Information'.center(50))
print('input 6: Exit'.center(50))
stus = []
while True:
    operate = input("Please input the number you want to do")
    if operate == "1":
        name = input("please input the name")
        age  = input("please input the age")
        qq   = input("please input the qq")
        stu={}
        stu["name"] = name
        stu["age"]  = age
        stu["qq"]   = qq
        stus.append(stu)
    if operate == "2":
        name = input("Input the name you want to find")
        for item in stus:
            if item ["name"] == name.strip():
                print("%s student exis， age is %s, qq is %s"%(item["name"],item["age"], item["qq"]))
                break
        else:
                print("no such name")
    # if operate == "3":

    if operate == "5":
        print("ID\tName\tAge\tQQnumber")
        for i,item in enumerate(stus,1):
            print("%s\t%s\t%s\t%s"%(i,item["name"],item["age"],item["qq"]))