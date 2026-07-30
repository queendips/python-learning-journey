# Create a new text file using Python.
file = open("demo.txt" , "w")
file.close()  #oses the file and saves any changes.
print("We have created our first file successfully")

# If the file doesn't exist, Python creates it.
# If the file already exists, Python opens it and clears all existing content.

# Write Multiple Lines
file = open("student.txt", "w")
file.write("Name: Dipali\n")
file.write("Course: Python\n")
file.close()
print("data saved in file")