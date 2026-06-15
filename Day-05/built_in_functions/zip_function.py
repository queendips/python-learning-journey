names = ["Rahul", "Priya", "Amit"]
marks = [85, 92, 78]

result = zip(names, marks)

print(list(result))

#------------
servers = ["web1", "web2", "db1", "db2"]
status = ["UP", "DOWN","UNKNOWN","WARNING"]

for server , state in zip(servers,status):
    print(server, state)

#-------------------
products = ["Laptop", "Mouse", "Keyboard"]
prices = [50000, 500, 1500]

for product, price in zip(products, prices):
    print(product, price)