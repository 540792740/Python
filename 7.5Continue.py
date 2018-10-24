i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        print("%d is an even number"%i)
        continue
    print("%d is an odd number" %i)