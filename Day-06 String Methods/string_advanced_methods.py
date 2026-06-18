# partition()

# Splits the string into 3 parts:

# Before separator
# Separator
# After separator
text = "Python-Programming"

print(text.partition("-"))

# rpartition()
# Works like partition(), but starts searching from the right.
text = "one-two-three"

print(text.rpartition("-"))

# maketrans()

# Creates a translation table.
table = str.maketrans("abc", "123")

print(table)
# translate()

# Replaces characters using a translation table.
table = str.maketrans("abc", "123")

text = "abc"

print(text.translate(table))

# casefold()

# Similar to lower(), but more aggressive for case-insensitive comparisons.
text = "PYTHON"

print(text.casefold())

# encode()

# Converts a string into bytes.

print(text.encode())

# format_map()

# Formats a string using a dictionary.
data = {
    "name": "Dips",
    "role": "DevOps Engineer"
}

text = "Name: {name}, Role: {role}"

print(text.format_map(data))