import csv
new_employees = [
    [103, "Priya", "Finance"],
    [104, "Amit", "Sales"]
]
with open("employees.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_employees)
print("Employees added successfully.")