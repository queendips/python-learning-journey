with open("student.txt", "r+") as file:
    print(file.read())
    file.write("\nCity: Pune")
    print(file.read())