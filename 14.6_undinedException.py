class PasswordException(Exception):
    def __init__(self, pw, min_length):
        self.pw = pw
        self.min_length = min_length
    def __str__(self):
        return "Password is less than 6 characters"

def reg(username,password):
    if len(password) < 6:
        raise PasswordException(password,6)
    else:
        print("UserName: %s, password: %s"%(username,password))

try:
    reg("zs","123")
except Exception as ex:
    print(ex)
except PasswordException as ax:
    print("second", ax)