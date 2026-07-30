import json
# json.load()
# Reads JSON from a file.
with open("students.json", "r") as file:
    data = json.load(file)
print(data)

# json.loads()
# Here, the JSON is not in a file. It's just stored in a Python string.
json_string = '{"name":"Dipali","age":25}'
data = json.loads(json_string)
print(data)