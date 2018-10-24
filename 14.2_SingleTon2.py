class User(object):
    __instance = None
    def __init__(self, name):
        self.name = name

    # __new__ methon only run 1 time, others can be return cls.instance
    def __new__(cls, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls) #create present class object
        return cls.__instance

u1 = User('jw')
u2 = User('MX')
print(u1.name)
print(u2.name)
print("u1对象的内存地址： %s, Memory address of object U2 %s"%(id(u1),id(u2)))