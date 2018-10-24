print('='*30)
print('Student Management System'.center(50))
print('input 1: Add a Student Name')
print('input 2: Find a Student Name')
print('input 3: Change a Student Name')
print('input 4: Remove a Student Name')
print('input 5: Exit')

Students = ['Bob']
while True:
    operate = input('Input a number: ')
    if operate == '1':
        name = input('Please Input the Name')
        Students.append(name.strip()) #输入有空格的话去掉
        print(Students)
    if operate == '2':
        name = input('please Input the name who you want to find')
        print(name in Students)
    if operate == '3':
        name = input('please Input the name who you want to change')
        afterName = input('pleas input the new name')
        Students.remove(name.strip())
        Students.append(afterName.strip())
        print(Students)
    if operate == '4':
        name = input('input the name you want to remove')
        if name not in Students:
            print(name + ' is not in the list')
        else:
            Students.remove(name)
            print(Students)

    if operate == "5":
        break
