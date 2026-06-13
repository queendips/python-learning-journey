def student (name, age=20):
    print("Name", name)
    print("Age", age)
student("Bob")
student("Raju", 25)

#Power Function
def power(num, exponent = 2):
    return num ** exponent
print(power(5))
print(power(5, 4))

# Bill Calculation
def calculate_bill(amount, tax=18):
    total = amount + (amount * tax / 100)
    return total

print(calculate_bill(1000))
print(calculate_bill(1000, 25))