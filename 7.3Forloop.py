i = 1
sum = 0
while i < 100:
    if i % 2 == 0:
        sum += i
    else:
        pass
    i += 1
print(sum)

x = 1
y = 1
while y <= 10:
    if y == 1 or y == 10:
        x = 1
        while x <= 10:
            print("*", end = "") #结尾是不回车
            x += 1
        print()
        y += 1
    else:
        print("*        *")
        y+=1
print("finish")