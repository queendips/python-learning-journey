import json
with open("student.json", "r") as file:
    data = json.load(file) #It returns a Python dictionary.
    print(data)
    print(type(data))
    print(data["name"])
# ----------------------------------------------
# ----------------------------------------------
with open("employees.json", "r") as file:
    employees = json.load(file)
    for employee in employees:
        if employee["id"] == 101:
            print("ID:", employee["id"])

# Print employees whose department is IT or Finance
with open("employees.json", "r") as file:
    employees = json.load(file)
for employee in employees:
    if employee["department"] == "IT" or employee["department"] == "Finance":
        print(employee)
        
# OR
for employee in employees:
    if employee["department"] in ["IT", "Finance"]:
        print(employee["name"], "-", employee["department"])