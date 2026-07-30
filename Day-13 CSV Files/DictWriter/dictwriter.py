# DictWriter writes dictionaries to a CSV file.
import csv
with open("employees.csv", "w", newline="") as file:
    fieldnames = ["ID", "Name", "Department"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "ID": 101,
        "Name": "Dipali",
        "Department": "IT"
    })
    writer.writerow({
        "ID": 102,
        "Name": "Rahul",
        "Department": "HR"
    })