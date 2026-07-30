import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Read Only the Header
print("Read Only the Header")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)
 
# Skip the Header
print("Skip the header")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

# Access Individual Columns
print("Access Individual Columns")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(f"{row[1]} age is {row[2]}")
        print("Name:", row[1])
        print("Course:", row[3])
        print("-----------")
      