file = open("student.txt", "r")

content = file.read()

print(file.readable())   
print(file.writable())   

print(content)

file.close()
# ---------------------------
file = open("student.txt", "w")

file.write("Hello Python")

print(file.readable())   # False
print(file.writable())   # True

file.close()