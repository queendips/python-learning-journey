# replace()
# Replaces one substring with another.
text = "JS is my favorite programming langauge"
print(text.replace("JS" , "Python"))

# split()
# Splits a string into a list.

print(text.split(","))

fruits = "apple,banana,mango"
print(fruits.split(","))

# rsplit()
# Splits from the right side.
text = "one-two-three-four"

print(text.rsplit("-", 1))

# splitlines()
# Splits a string at line breaks.

text = "Python\nJava\nGo"

print(text.splitlines())

# join()
# Joins elements of a list into a string.
languages = ["Python", "Java", "Go"]

print(", ".join(languages))

# --------------------------------
servers = "server1,server2,server3"

server_list = servers.split(",")

print(server_list)