#str 不可变， list 可变。
a = 'abc'
a  = a.replace('a','A')
print(a)

a = [1,2] #list
b = a
b +=[2,3]
print(a)
print(b)
print(id(a))
print(id(b))
#只想同一块内存
a = [1,2] #list
b = a
b = b + [2,3]
print(a)
print(b)
print(id(a))
print(id(b))
#############################################
# 针对可变类型     a += 11   !=  a = a + 11   #
##################################3##########
# 针对不可变类型 这两个是一样的

a = [1,2,3,4,5]
print(max(a))
print(len(a))
print(min(a))
b = 2
print(chr(97))

str = input('input a string')
res = {}
for i in str:
    if i  in res:
        res[i] += 1
    else:
        res[i] = 1
print(res)
################################################
# list
name = []   #list   name[0] = value
name = ()   #tuple  不能改变
name = {}   #dict(key: value# ) name[key] = value

















