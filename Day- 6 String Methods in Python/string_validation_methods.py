# isalpha()
# Returns True if all characters are alphabets.
text = "India"

print(text.isalpha())
text = "India@123"

print(text.isalpha())
# digit()
text = "34567"
print(text.isdigit())
# isalnum()
text1 = "India@123"
print(text1.isalnum())

text = "Abc123"

print(text.isalnum())

# isspace()
# Returns True if the string contains only spaces.

# isspace()
# Returns True if the string contains only spaces.

text = "   "

print(text.isspace())

# islower()
# Checks whether all letters are lowercase.
text = "python is very easy lang"
print(text.islower())

# isupper()
# Checks whether all letters are uppercase.
text = "PYTHON"
print(text.isupper())

# istitle()
# Checks whether each word starts with a capital letter.

message = "I Am From India"
print(message.istitle())

# isdecimal()
# Checks whether all characters are decimal numbers.
num = "5647"
print(num.isdecimal())

# isnumeric()
# Checks whether all characters are numeric

print(num.isnumeric())

# isidentifier()
# Checks whether a string is a valid Python variable name.

text = "user_name"

print(text.isidentifier())
text = "123name"

print(text.isidentifier())
# --------------------------------------

username = input("Enter username: ")

if username.isidentifier():
    print("Valid username")
else:
    print("Invalid username")