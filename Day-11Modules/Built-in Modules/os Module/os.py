# os.getcwd()
# Returns the Current Working Directory
import os
print(os.getcwd())

# os.chdir()
# Changes the current working directory.
# os.chdir(path)
os.chdir("F:\python-learning-journey")
print(os.getcwd())

# os.mkdir()
# Creates a new folder.
#syntax:os.mkdir("FolderName")
# os.mkdir("Project1")

# os.makedirs()
# Creates multiple nested directories at once.
# os.makedirs("Project2/data")

# os.listdir()
# Returns all files and folders in a directory.
print(os.listdir())

# os.rename()
# Renames a file or folder.
#syntax:os.rename(old_name, new_name)
# os.rename("project2", "project5")
# os.remove()
os.remove("Project1")
# os.rmdir()

# Deletes an empty directory.
os.rmdir("Projects")
# os.path.exists()
# Checks whether a file or folder exists.

print(os.path.exists("demo.txt"))

# os.path.join()
# Joins file paths correctly for your operating system.
path = os.path.join("Python", "Day11", "example.py")
print(path)

# os.environ
# Accesses environment variables.
print(os.environ.get("USERNAME"))

# os.system()
# Runs an operating system command.
os.system("dir")
os.system("ls")