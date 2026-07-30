import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age", "Course"])
    writer.writerow([1, "Dipali", 25, "Python"])
    writer.writerow([2, "Rahul", 28, "Java"])
    writer.writerow([3, "Sam", 28, "SQL"])

# Writing Many Rows – writerows()
print("Writing Many Rows – writerows()")
data = [
    ["ID", "Name", "Age", "Course"],
    [1, "Dipali", 25, "Python"],
    [2, "Rahul", 28, "Java"],
    [3, "Priya", 25, "Data Science"],
	[4, "Sam", 30, "SQL"]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)