# any() is a built-in function that returns True if at least one value is True .
# 0 = False & Any non-zero number = True
# ----------------------------
values = [False, False, False]

print(any(values))
# ---------------------------
numbers = [0, 0, 5, 0]

print(any(numbers))
# ---------------------------------------------
marks = [35, 45, 28]

print(any(mark >= 40 for mark in marks))
# -----------------------------------
server_status = ["up", "up", "down"]

print(any(status == "down" for status in server_status))


# any() → At least one True → True