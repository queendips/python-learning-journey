values = [True, True, True]

print(all(values))

# -------------------------------------
values = [True, False, True]

print(all(values))
# ---------------------------
servers = ["up", "up", "up"]

print(all(status == "up" for status in servers))


# all() → All must be True → True