# f = open("11.3test1.txt","w")
# f.write("hello\tWorld")
# f.close()
f = open("11.3test1.txt","r")
content = f.read(5) #读五个字节
print(content)
content = f.read(6)
print(content)
f.close()

#open the file
f = open("11.3test1.txt",  "r")
content = f.read()

# open the file which can be writen
dest_f = open("11.3copy","w")

# write content to destination
dest_f.write(content)

dest_f.close()
f.close()

f = open("11.3test1.txt", "r")

a = open("11.3test1.txt","r")
content = f.read()

destination = open("11.3-copy", "w")
destination.write(content)
destination.close()
a.close()

f = open("11.3copy","r")
content = f.read(1)
print(content)

f.seek(3,0)
content = f.read(6  )
print(content)

