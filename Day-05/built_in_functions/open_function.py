# open() is a built-in function used to open files in Python.

# Creates a file and writes data

file = open("demo.txt", "w")

file.write("Hello, this is my first file in Python")

file.close()

# Read a File

file = open("demo.txt", "r")

content = file.read()
print(content)

file.close()

# Append Data

file = open("demo.txt", "a")

file.write("\nAdding new line using append mode")

file.close()


# Using with open()
with open ("demo.txt" , "r") as file:
    content = file.read()
    print(content)

# -----------------------------------------
with open("app_log.txt", "w") as log:
    log.write("Application started\n")
    log.write("User logged in\n")