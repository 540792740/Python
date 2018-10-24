# contains two "_" means private
# or Public
# as we can see __password is private ,cannot be used out of method

class User:
    def __init__(self, pw):
        if len(pw) < 5:
            print("len is too short")
        else:
            self.__password = pw

    def __str__(self):
        return "User name is %s, password is %s"%(self.Username, self.__password)

    def set_password(self, pw):
        if len(pw) >= 6:
            self.__password = pw
        else:
            print("Your password is less than six charater")
    def say_hello(self):
        print(self.password)

u1 = User("1234567678")
u1.Username = "VISA hope you can get soon"
# u1.set_password("1238894")
# u1.say_hello()

print(u1)