# count()

fruits = ("orange", "banana", "mango", "banana", "apple")
print(fruits)
count_banana = fruits.count("banana")
print(count_banana)

# index()
servers = ("web-1", "web-2","db-1","db-2","kong-1","kong-2")
print(servers)
server_position = servers.index("db-1")
print(server_position)
# sorted
numbers = (40, 10, 30, 20)

print(sorted(numbers))

#----------------
cpu_usage = (85, 77, 90, 89, 76)

print("Total Readings:", len(cpu_usage))
print("Highest Usage:", max(cpu_usage))
print("Lowest Usage:", min(cpu_usage))
print("Total Usage:", sum(cpu_usage))
print("Sorted Usage:", sorted(cpu_usage))