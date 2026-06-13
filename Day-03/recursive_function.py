# recursive function is a function that calls itself.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(4))

#countdown
def birthday_countdown(days):
    if days > 0:
        print(days , "days left for birthday")
        birthday_countdown(days-1)
    else:
        print("Happy Birthday:)")
birthday_countdown(5)