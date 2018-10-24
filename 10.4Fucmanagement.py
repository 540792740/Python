def print_menu():
    print()
    print('=' * 30)
    print('Student Management System'.center(50))
    print('input 1: Add a Student Name'.center(50))
    print('input 2: Find a Student Name'.center(50))
    print('input 3: Change a Student Name'.center(50))
    print('input 4: Remove a Student Name'.center(50))
    print('input 5: Display all Students Information'.center(50))
    print('input 6: Exit'.center(50))

Stus = []
def add_student():
    name = input("Please input a name")
    age = input("Please input an age")
    qq = input("Please input QQ number")
    stu = {}
    stu["name"] = name
    stu["age"] = age
    stu["qq"] = qq
    Stus.append(stu)
    print("Success")

def Search_name(name):
    if Stus:
        for item in Stus:
            if item["name"] == name.strip():
                print("Exist---------------------------")
                print_student(item)
                # break
                return item
            else:
                print("No, there is no such student")
        else:
            print("error")

def del_student(name):
    student = Search_name(name)
    if student:
        Stus.remove(student)
        print("Delete Successful")
    else:
        print("no such person")
def print_student(item):
    print("%s\t\t%s\t\t%s"%(item["name"],item["age"],item["qq"]))
    # print("The name is %s"%item["name"])
    # print("The age is %s"%item["age"])
    # print("The Qq is %s"%item["qq"])
def print_all_student():
    print("Number\tname\tage\t\tQQ")
    for i,item in enumerate(Stus,1):
        print("%s\t\t"%i,end = "")
        print_student(item)

print_menu()
while True:
    operate = input("Tell me the statement number what you want")
    if operate == "1":
        add_student()
    if operate == "2":
        Search_name()
    if operate == "4":
        name = input("Please input the student you want to delete")
        del_student(name)
    if operate == "5":
        print_all_student()
    if operate == "6":
        break

