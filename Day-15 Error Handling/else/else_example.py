try:
    result = 100 / 5

except ZeroDivisionError:
    print("Error")

else:
    print(result)

# -------------------------------------------------
# --------------------------------------------------

try:
    file = open("student.txt", "r")

except FileNotFoundError:
    print("File not found.")

else:
    print(file.read())
    file.close()