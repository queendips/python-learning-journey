# Suppose you're creating a banking application.
# A user enters:
# Withdraw Amount = -1000
# Python doesn't know that this is invalid because -1000 is still a valid integer.
# if amount < 0:
#     raise ValueError("Amount cannot be negative.")

# Common Exceptions You Can Raise
# Common Exceptions You Can Raise
# raise TypeError("Invalid type")
# raise ValueError("Invalid value")
# raise IndexError("Invalid index")
# raise KeyError("Key not found")
# raise Exception("Something went wrong")
# ========================================================
age = int(input("Enter age: "))

if age < 18:
    raise ValueError("You must be at least 18 years old.")

print("Eligible")

# =================================================================

balance = 5000
withdraw = int(input("Enter withdrawal amount: "))

if withdraw > balance:
    raise ValueError("Insufficient balance.")

print("Withdrawal Successful")