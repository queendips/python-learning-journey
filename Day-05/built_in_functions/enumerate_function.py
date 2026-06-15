students = ["Raju", "Rahul","Bob", "Shyam"]

for roll_no, student in enumerate(students, start=101):
    print(roll_no, student)

#----------------
# names = ["Rahul", "Priya", "Amit"]

# for item in enumerate(names):
#     print(item)  #By default, index starts from 0

logs = ["Start", "Deploy", "Error", "Restart"]

for i, event in enumerate(logs, start=1):
    print("Event", i, ":", event)