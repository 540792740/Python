names = ["jiawei", "mingxin", "zeyu"]
names2 = names
student = {"name" : "Jiawei"}    #dict
a = "my favorite"
b =  2
def test1():
    print("The original ver: %s"%names)
    names[2] = "jian"
    student["age"] = "12"
    print(names)
    print(student)
    global a
    a = "Cristiano"
    global b
    b = b + 1
test1()
print(a)
print(b)

a =  [1,2]
print(id(a))
a.insert(1,5)   #第一个位置插入5
print(a)
print(id(a))
a = [4,5]
print(id(a))
#######################################
#返回多个结果
#用元祖可以,列表也可以
def test1():
    a = 1
    b = 2
    return [a,b]
x = test1()
print(x)

def test2(x,y,z = 10, d = 1):
    return x + y + z
x = test2(1,1)
print(x)
###################
print("-------------")
def test1(x,y,*args, z = 20):
    print(args)
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)
test1(1,2,3,4,4,5,6,z = 10)

def test2(x, y, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)
    sum = 0
    for i in kwargs.values():
        sum = sum + i
    print(sum)
test2(2,3,4,5,6,7,8, num1 = 1, num2 = 2)

nums = [3,4]
num1 = {"num1" : 5, "num2" : 6}
def test3(x, y, *args, **kwargs):
    sum = 0
    print(x)
    print(args)
    print(kwargs)
test3(1,2,3,*nums, **num1  )