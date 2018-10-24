fuc = lambda x,y:x+y
print(fuc(11,22))

def test(a, b, fuc):
    result = fuc(a, b)
    return result
print(test(22,33, lambda x,y: x+y))

#sort
a = [1,2,34,8,2,77,22]
a.sort()
print(a)
a.sort(reverse = True)
print(a)
#######################################
#        a.reverse是反转，不是排序      ##
#######################################


stus =[{"name" : "wjw", "age" : 23},{"name": "MX", "age" : 21}]
# stus.sort(key = lambda x:x["name"])
stus.sort(key = lambda x:x["age"])
print(stus)