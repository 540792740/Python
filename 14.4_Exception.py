try:
    print(a)
except NameError:
    print("Name exception")

# Format Error
a = "12345"
# a = 12345
f = open("14.4_Exception_text.txt", "w")
try:
    f.write("Hello\n")
    f.write("World %d"%a)

except Exception as ex:
    print(ex)
#     All the exception, catch all of them

else:
    print("No error")
finally:
    print("Finally")
    f.close()

#Open File
a = "123"
try:
    f = open("Test2.txt", "w")
    f.write("Happy")
    f = open("Test2.txt", "r")

    try:
        content = f.read()
        content.index("Happy")
        content.index("Hadoop")
    except ValueError as ex:
        print(ex)

except FileNotFoundError as ex:
    print(ex)




