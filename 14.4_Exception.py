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
else:
    print("No error")
finally:
    print("Finally")
    f.close()