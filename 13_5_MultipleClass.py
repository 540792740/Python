class User(object):
    name = "username"
    __password = "123"  #Private, we cannot use it out the class

    def __init__(self, sex, unsername):
        self.sex = sex
        self.unsername = unsername

u = User("Male", "Cristiano")
print(u.name)
u2 = User("Female", "cc")
# print(u2.__password)  #error,private
print("--" * 30)


class QQ_user(User):
    pass

print(QQ_user.name)

# Change the name of the className
# 1.Wrong:
print("Change the name of object:", end = " ")
u.name = "CR7"
print(User.name)
User.name = "Cr7"
print("change the name of Class", end = " ")
print(User.name)