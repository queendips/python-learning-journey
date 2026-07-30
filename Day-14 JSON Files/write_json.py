import json

student = {
    "id": 1,
    "name": "Dipali",
    "age": 25,
    "course": "Python"
}
with open("student.json", "w") as file:
    # json.dump(student, file)
    json.dump(student, file, indent=4)
print("JSON file created successfully.")

# -----------------------------------------------
# Write a List of Dictionaries
print("Write a List of Dictionaries")

employees = [
    {
        "id": 101,
        "name": "Rahul",
        "department": "HR"
    },
    {
        "id": 102,
        "name": "Dipali",
        "department": "IT"
    },
    {
        "id": 103,
        "name": "Priya",
        "department": "Finance"
    }
]
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)