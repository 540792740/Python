def fxd(a,b = "No", c = "Argument"):
    print(a,b,c)
a = fxd(22)

var = "this is a string"
print(var[3:6])

text = "python"
for alphabet in text:
    print(alphabet)

n = int(input("input the line"))
a = 0
b = n
while a <= n:
    print(a*" ", end = "")
    while b > 0:
        print((b-1)*"* " + "*",end = " ")
        b -= 1
        break
    print()
    a = a+1