try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")