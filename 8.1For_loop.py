# for i in "abcdef":
         # print(i)
# else:
#     print("no")
#
# for i in range(1,10):
#     print(i)

name = 'abcdefghijklmn'
print(name[0::2])
print(name[0::3])
i = len(name) -1
while i >= 0:
    print(name[i],end = "")
    i -= 1
print()
print(name[-1::-1])