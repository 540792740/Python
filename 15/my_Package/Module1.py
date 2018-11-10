# 15.1

# Write a function, judge String is or not null
#是否对外公开，只有all里面的函数可以被调用，其他的不行
__all__ = ["isNull","text"]

def isNull(str):
    if not str:
        return True

    elif str.strip() == '':
        return True
    else:
        return False

def text():
    print("In Module1")

# import时不调用的东西控制方法
if __name__ == "__main__":
    print("Excute")

# print("ppppp")