try:
    file = open("student.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("The file does not exist.")