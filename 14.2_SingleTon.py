class User(object):
    __instance = None
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instance(cls,name):
        if not cls.__instance:
            cls.__instance = User(name)
        return cls.__instance

u1 = User.get_instance("jw")
u2 = User.get_instance("mx")
print(u1 == u2)
print("u1对象的内存地址： %s, Memory address of object U2 %s"%(id(u1),id(u2)))
print(u1)
print(u2)

u1 = User("jw")
u2 = User("mx")
print(u1 == u2)
print("u1对象的内存地址： %s, Memory address of object U2 %s"%(id(u1),id(u2)))