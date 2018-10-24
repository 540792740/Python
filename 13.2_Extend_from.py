class Animal:
    def __init__(self):
        self.color = "Yellow"
        print("initialize")

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class dog(Animal):
    def __init__(self, name):
        self.__name = name
        super().__init__()
        print("initialize %s"%name)

    def eat(self):
        print("Dog Eating")


    def Shout(self):
        print("Bark...Bark...")

class cat(Animal):
    def catch(self):
        print("catch the mouse")

dog = dog("BabyDog")
print(dog.color)
dog.eat()
print("-" * 30)
# 私有属性，__,不能轻易修改

# __init__() 就是构造器.初始化变量的作用。

class User:
    def __init__(self):
        print("inicializing")

    def __del__(self):
        print("Delete object")

u = User()
u2 = u
# del u
print("-" * 30)
# del u2
