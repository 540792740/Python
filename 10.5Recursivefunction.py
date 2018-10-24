#阶乘
result = 1
i = 1
while i <= 4:
    result = result * i
    i = i + 1

print(result)


def recs(n):
    if n <= 1:
        return 1
    else:
        return n * recs(n - 1)

print(recs(5))