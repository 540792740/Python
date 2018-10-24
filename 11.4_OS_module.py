import os

# 显示绝对路径
content = os.path.abspath("11.3copy")
print(content)

# 显示文件大小
content = os.path.getsize("11.3copy")
print(content)

file_list= os.listdir("txt/")
# print(file_list)
while(True):
    a = input("Choose the way you want \n '1' means delete re \n '2' means add re ")
    if a == "1":
        for f in file_list:
            filePath = os.path.join("txt/", f)
            if os.path.isfile(filePath):
                Name_split = f.split("-")[0]
                # print(Name_split)
                os.rename(filePath, "txt/" + Name_split)
        break
    if a == "2":
        for f in file_list:
            dest_name = f + "-re"
            # print(dest_name)
            os.rename("txt/" + f, "txt/" + dest_name)
        break
