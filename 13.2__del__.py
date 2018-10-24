class user:
    def __init__(self):
        print("successful")
    def __del__(self):
        print("delete Successfully")

u = user()
u2 = u


del u
# Right now, the memory is not delete
print("-" * 20)
del u2
# When delete u2, all the memory can be delete
