import sys

print(sys.argv)

a = [1 for i in range(1,9)]
print(a)

a = [i for i in range(1,9)]
print(a)

a = [i**2 for i in range(1,9)]
print(a)

a = [x for x in range(1,3) for y in range(0,2)]
print(a)
# 1循环两次，2循环两次

a = {(x,y) for x in range(1,3) for y in range(4,5)}
print(a)

a = {(x,y,z) for x in range(1,3) for y in range(4,5) for z in range (4,6)}
print(a)

a  = [i for i in range(4,10) if i%2 ==1]
print(a)