# index()
# The index() method returns the position (index) of the first occurrence of a value in the list.
fruits = ["apple", "banana", "apple", "mango"]
position = fruits.index("banana")
print(position)

colors = ["red", "blue", "red", "green"]

print(colors.index("red"))
# print(colors.index("pink"))

# -----------------------------------------------------------

servers = ["web-server", "app-server", "db-server"]

server_position = servers.index("db-server")

print("Database server is at index:", server_position)