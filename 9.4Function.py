#重复执行的代码，单独命名一个函数，提高代码利用率
def print_hello():
    print("Life is short, we need learn Python")
print_hello()

def test(r):
    s = 3.14 * (r**2) #r的幂pi * r^2
    print("Area is %s" %s)

test(9.8)

def test1(a,b): #a,b为形参，有真实数值的叫实参。
    if not isinstance(a,(int,float)):
        print("we cannot use a")
        pass

    elif not isinstance(b,(int, float)):
        print("we cannot use b")
        return
    else:
        sum = a + b
        print("%s + %s = %s"%(a,b,sum))
test1("ss","kk")

def test2(a):
    print(isinstance(a,(int,float)))
test2("sds")

print("_______________")
def avg(a,b,c):
    if is_number(a) and is_number(b) and is_number(c):
        return (a + b + c) / 3
    else:
        print('error')

def is_number(a):
    if not isinstance(a,(int,float)):
        print("wrong")
        return
    else:
        return True
avg(1,2,"l")
print("-----------------")
#######################
a = 400
def test1():
    a = 200
    print(a)
test1()
print(a)
#函数改变的是局部变量，如果有return
############################
def test2():
    a = 300
    print(a)
    return a
b = test2()
def test3(b):
    a = b + 1
    print(a)
test3(b)