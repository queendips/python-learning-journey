# readline()
file = open("student.txt", "r")

print(file.readline())

file.close()
# readlines()
file = open("student.txt", "r")

data = file.readlines()

print(data)
print(file.readline().strip())

file.close()