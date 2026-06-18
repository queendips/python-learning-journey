# count()
# The count() method returns the number of times a specified value appears in a list.
fruits = ["apple", "banana", "apple", "mango"]
result = fruits.count("apple")
print(result)

# ----------------------------------

servers = ["running","unknown", "running", "not reachable", "down", "running"]
print(servers.count("running"))

# ----------------------------------
build_status = ["SUCCESS", "FAILED", "SUCCESS", "FAILED", "FAILED"]

failed_count = build_status.count("FAILED")

print("Failed builds:", failed_count)