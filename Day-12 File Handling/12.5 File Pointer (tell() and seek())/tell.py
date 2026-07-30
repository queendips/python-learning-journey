# tell() returns the current position of the file pointer.
with open("student.txt", "r") as file:
    print(file.tell())

#0 --> The pointer is at the beginning of the file.
with open("student.txt", "r") as file:
    print(file.read(5))
    print(file.tell())