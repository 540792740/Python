my_str = "hello world, just like a beauty walking in the night"
print(my_str.find("like"))  #关键词位置,找不到返回-1
print(my_str.index("like")) #关键词位置，和find一样，没有会抱错
print(my_str.rindex("like"))
print(my_str.count("like")) #有几个“like”出现
print(my_str.replace("like", "dislike")) #替换

print(my_str.split(" "))    #分成数组
print(my_str.split(" ",2))  #分成数组，最多成为3个
print(my_str.partition("like")) #分成数组，其中like也是一个部分

print(my_str.capitalize())   #首字母大写

name = "he llo \tsdfds\tsins \nskk "
# 怎样用“空格和制表符两个东西隔开

print(name.split()[-2])



name = "     abcdefghigklmn     "
print(name.strip()) #去左边空格掉两边空格
print(name.lstrip())#去掉左边的空格
print(name.rstrip())


line = "abc\nefg\nhig"
print(line.splitlines(), end = " ")#换行分符割并写成一个列表
print(line.split("\n"), end = " ") #换行符分割并写成列表
linetable = line.split("\n")
print("-".join(linetable))#把一个“-” 字符串放在每个元素后面，连起来

is_alpha = "aaa"
is_bate  = "a a"
is_lambda= "a1a"
print(is_alpha.isalpha(),end = " ")   #isalpha: 如果字符串全是字母，true
print(is_bate.isalpha(),end = " ")    #有空格， false
print(is_lambda.isalpha())  #有数字， false

is_lambda= "123"
print(is_alpha.isdigit(),end = " ")   #isdigit: 字符串全是数字，true
print(is_lambda.isdigit())   #有其他任何东西都是false

is_lambda = "aa1"
print(is_lambda.isalnum)    #isalnum: 只有数字和字母，没有符号和空格，true

is_lambda = "   "
print(is_lambda.isspace())