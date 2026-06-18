# sort()
# The sort() method sorts the items of a list in ascending order by default.

employee_ids = [105, 101, 103, 102, 104]
employee_ids.sort()
print(employee_ids)
employee_ids.sort(reverse=True)
print(employee_ids)
new_list = sorted(employee_ids)
print(employee_ids)
print(new_list)