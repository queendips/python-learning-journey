# union()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {10,11}

print("Union of sets:", set1 | set2)
print("Symmetric difference:", set1 ^ set2)
# result = set1.union(set2)
result = set1.union(set2, set3)

print(result)

# intersection()
print("Intersection of sets:", set1 & set2)
result = set1.intersection(set2)

print(result)
# -------------------------------------------------
# difference()
day1 = {"Rahul", "Amit", "Priya", "Neha"}
day2 = {"Priya", "Neha"}

absent_day2 = day1.difference(day2)

print(absent_day2)
result = set1 - set2

print(result)

# symmetric_difference()
java_team = {"Rani", "Rahul", "Amit"}
python_team = {"Jaya", "Komal", "Sameer"}

unique_members = java_team.symmetric_difference(python_team)

print("Unique Team Members:", unique_members)

print(result)
#----------------------------------------------------
#add()
employee_ids = {101, 102, 103}

employee_ids.add(104)

print(employee_ids)

#update()
employee_ids.update([105,106,107])
print(employee_ids)

#remove()
# The remove() method removes a specified item from a set.
employee_ids.remove(107)
print(employee_ids)

#discard()
# The discard() method removes a specified item from a set.
# The difference is that discard() does not raise an error if the item is not found.
employee_ids.discard(106)
print(employee_ids)

#pop()
# The pop() method removes and returns a random item from the set.

participants = {"Raju", "Amit", "Bob"}

winner = participants.pop()

print("Winner:", winner)     #Since sets are unordered, you cannot predict which item will be removed.
print("Remaining Participants:", participants)

# list, pop() removes an item by index but  in set pop() removes a random item because sets do not have indexes.

# clear()
# clear() removes all elements but keeps the set.
fruits = {"Apple", "Banana"}

fruits.clear() 

print(fruits)

# delete()
# deletes the entire set variable. Variable is completely removed from memory.
# del fruits 
print(fruits)

# copy()
# The copy() method creates a shallow copy of a set.
employee_ids = {101, 102, 103}

backup_ids = employee_ids.copy()

backup_ids.add(104)

print("Original:", employee_ids)
print("Backup:", backup_ids)