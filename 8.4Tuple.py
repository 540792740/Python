#tuple元祖不能修改，长度固定。
# 用的是（）小括号
my_str = ['aaa', 'bbb', 'ccc']
# my_str[0] = 'abcde'不能修改
print(my_str[0])
print(len(my_str))

mt_tuple = (100,200,my_str)
mt_tuple[2][0] = 100
print(mt_tuple[2][0])       #修改tuple中第三个list里面的值
# []是list
# ()是tuple

i = 1
while i < 10:
    if i < 6:
        print(i * "*")
        i = i+ 1
    else:
        print((10 - i) * '*')
        i = i + 1

for i in mt_tuple:
    print(i)
i = 0
while i < len(mt_tuple):
    print(mt_tuple[i])
    i = i + 1