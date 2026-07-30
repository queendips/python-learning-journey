try:
    number = int(input("Enter a number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("Invalid input.")

    # ---------------------------------
try:
    age = int(input("Enter your age: "))
    result = 100 / age

    print(result)

except ValueError:
    print("Age must be a number.")

except ZeroDivisionError:
    print("Age cannot be zero.")