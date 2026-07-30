with open("student.txt", "a+") as file:
    file.write("\nCourse: Python")
    file.seek(0)
# seek(0) is needed because after appending, the pointer is at the end of the file.
    print(file.read())