employee = {
    "id": 101,
    "name": "Dipali",
    "role": "DevOps"
}

print(employee.get("name"))
print(employee.keys())
print(employee.values())
print(employee.items())

# update()
employee.update({"role": "Senior DevOps Engineer"})
employee.update({"city": "Nagpur"})

#or#
employee.update({
    "Project": "Gloo",
    "shift": "General"
})
print(employee)

# pop()
employee.pop("city")
print(employee)

# popitem()
removed_item = employee.popitem()
print(removed_item)
print(employee)

#cler()
# employee.clear()
# print(employee)

# copy()
new_employee = employee.copy()
print(new_employee)

# setdefault()
# setdefault() method returns the value of a key. If the key does not exist, it inserts the key with a default value.
print(employee.setdefault("city", "Nagpur"))
print(employee)





# ------------------------------------------------
config = {
    "server": "jenkins",
    "port": 8080
}
backup = config.copy()

backup["port"] = 9090

print("Original:", config)
print("Backup:", backup)