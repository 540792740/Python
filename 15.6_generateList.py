'''
[[1,2,3],[4,5,6],...]
'''

a = [[x,y,z] for x in range(1,100) if x%3 == 1 for y in range(1,100) if y %3 ==2  for z in range (100) if z % 3 ==0 if y-x ==1 and z - y == 1]
print(a)

a = [[i,i + 1, i+2] for i in range(1,100) if i % 3 == 1]
print(a)