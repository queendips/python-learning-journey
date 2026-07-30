# Features
# ✅ Creates a new file
# ❌ Raises an error if the file already exists

with open("sample.txt", "x") as file:
    file.write("New file created")