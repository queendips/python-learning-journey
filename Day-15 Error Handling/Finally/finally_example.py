# The finally block always executes, whether an exception occurs or not.
try:
    file = open("student.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    try:
        file.close()
        print("File closed.")

    except NameError:
        print("No file was opened.")