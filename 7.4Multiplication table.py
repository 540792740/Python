x = 1
y = 1
while x <= 9:
    y = 1
    while y <= x:
        print('%d*%d=%d  '%(x,y,x*y), end = "")
        y += 1
    print()
    x += 1

x = 1
y = 1
while x < 9:
    y = 1
    while y <= x:
        print('%d * %d = %d')