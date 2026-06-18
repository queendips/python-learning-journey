environments = ("dev", "test", "uat", "prod", "pt")

if "pt" in environments:
    print("PT env  is available")



# ------iteration-----------
servers = ("web01", "web02", "app01", "db01")

for server in servers:
    print("Checking server:", server)

#unpacking------------

server = ("web01", "Linux", "Running")

server_name, os_type, status = server

print("Server Name:", server_name)
print("OS:", os_type)
print("Status:", status)