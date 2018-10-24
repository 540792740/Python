import os

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

def add_student():
    name = input("Please input a name")
    age = input("Please input an age")
    qq = input("Please input QQ number")
    stu = {}
    stu["name"] = name
    stu["age"] = age
    stu["qq"] = qq
    stus.append(stu)
    print("Success")

def Search_name(name):
    if stus:
        for item in stus:
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
        stus.remove(student)
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
    for i,item in enumerate(stus,1):
        print("%s\t\t"%i,end = "")
        print_student(item)

def read_stus():
    if os.path.exists(file_name):
        f = open(file_name,'r')
        while True:
            student_str = f.readline()
            if student_str == '':
                break
            elif student_str.strip() != "" and student_str != "\n":
                student_info_list = student_str.split()
                student = {"name" : student_info_list[0], "age" : student_info_list[1],"qq" : student_info_list[2]}
                stus.append(student)
            print(stus)


def write_student_to_file():
    if os.path.exists(file_name):
        if os.path.exists(backup_file):
            os.remove(backup_file)
            os.rename(file_name, "backup-" + file_name)
    f = open(file_name, "w")
    for student in stus:
        student_str = '%s\t%s\t%s\n'%(student['name'],student['age'],student['qq'])
        f.write(student_str)
    f.close()


def main():
    print_menu()
    read_stus()
    while True:
        operate = input("Tell me the statement number what you want")
        if operate == "1":
            add_student()
            write_student_to_file()
        if operate == "2":
            Search_name()
        if operate == "4":
            name = input("Please input the student you want to delete")
            del_student(name)
            write_student_to_file()
            print("Delete Successful"%name)
        if operate == "5":
            print_all_student()
        if operate == "6":
            break

backup_file = "backup-12.1_file_name.txt"
stus = []
file_name = "12.1_file_name.txt"
main()

