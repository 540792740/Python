# dictionary

# 不能重复出现key
# 用的是{}大括号
dic = {'mIngxin': 21, 'Jiawei': 22, 'zeyu': 24}
dic['Jiawei'] = 21
#两种输出方法，get方法不报错，另一种报错。
print(dic.get('zeyu'))
print(dic.get('hello world'))
print(dic['zeyu'])

#写入,删除：
dic['Daijian'] = 27
del dic['Jiawei']

#判断是否存在：key in dic, 不能是value in dic
print('Jiawei' in dic)
print(dic)

# for i in dic.keys():
    # print(i)

print(len(dic))
print(dic.keys())
print(dic.values())
print(dic.items())

# 用for循环按顺序打印
for i in dic.items():
    print("key:%s \t value:%s"%i)

#判断是否在字典中：
key = 'Jiawei'
if key in dic:
    print('true')
else:
    print('error')
    print('error')