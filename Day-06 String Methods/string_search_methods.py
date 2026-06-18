# find()
# Returns the position of the first occurrence of a substring.
text = "Python Programming"

print(text.find("Programming"))
print(text.find("java"))

# rfind()
# Returns the position of the last occurrence of a substring.
text1 = "JS JS Programming"

print(text1.rfind("JS"))

# index()
# Works like find(), but raises an error if the value is not found.
print(text1.index("Programmin"))
# print(text1.index("python"))

# count()
# Counts how many times a substring appears.
print(text1.count("JS"))

# startswith()
# Checks whether a string starts with a given value.

print(text1.startswith("JS"))

# endswith()
# Checks whether a string ends with a given value.

print(text1.endswith("Programming"))

# ========================================

log = "error : Disk space is full"
if (log.startswith("error")) :
    print("Error detected")