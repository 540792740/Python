class User(object):
    def __init__(self,user,password):
        self.user = user
        self.password = password
        print("initialize")

    def __new__(cls,user,password):
        print("Create the object")
        return object.__new__(cls)
        # cls表示当前的类
    def __str__(self):
        return "Username %s, password %s"%(self.user,self.password)

u = User("WJW", "1232456")
# 先new出来，然后初始化
print(u)