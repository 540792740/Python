#list是有序集合，随时添加删除元素
# 用的是【】书括号

classmates = ['Michael', 'Bob', 'Kane']
name = ['Cone', 'Baby']     #元素顺序： 0，1，2
print(len(classmates))      # append, extend, insert
classmates.append('Nancy')
classmates.extend(name)
classmates.insert(0,'Number0')
classmates.insert(0,'Number0')
classmates.insert(0,'Number0')
classmates[0] = 'Number1'    #打印第0个
print(classmates)
print(classmates.count('Number0'))
print('Bob' in classmates)
del classmates[0]           #删除列表第0个数
classmates.remove('Bob')    #删除‘Bob’
print(classmates)
print(classmates.pop())

classmates.reverse()
print(classmates)

number = [23,1,5,22,62,2,6]
number.sort()
print(number)