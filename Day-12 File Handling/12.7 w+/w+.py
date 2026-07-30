# Features
# ✅ Read
# ✅ Write
# ✅ Creates the file if it doesn't exist
# ⚠️ Deletes all existing content before writing

with open("student.txt", "w+") as file:

    file.write("Hello Python")

    file.seek(0)

    print(file.read())