# json.dump()
# Writes a Python object to a file.
import json
student = {
    "name": "Dipali",
    "age": 25
}
with open("students.json", "w") as file:
    json.dump(student, file, indent=4)

# This creates or updates student.json.

# json.dumps()
# Converts a Python object into a JSON string.

student = {
    "name": "Dipali",
    "age": 26
}
json_string = json.dumps(student)
print(json_string)
# output is a string, not a file.
print(type(json_string))