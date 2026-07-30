# num1 = 10
# num2 = 0
# result = num1 / num2
# print(result)

# Output
# ZeroDivisionError: division by zero

# With try and except:
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(result)
except:
    print("Cannot divide by zero.")
print("Program Ended")