with open("student.txt", "r") as file:
    file.seek(0)
    print(file.read())