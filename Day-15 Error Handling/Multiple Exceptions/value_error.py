try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print(result)
except ValueError:
    print("Please enter only numbers.")