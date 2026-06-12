# Nested If Example
attendance = 60
fees_paid = True 
if attendance >= 75:
    if fees_paid:
        print("You are eligible for exam")
    else:
        print("Please pay fees")
else:
    print("Attendance is below 75%")

# Employee Bonus
experience = 4
performance = "Excellent"
if experience >= 5:
    if performance == "Excellent":
         print("Eligible for Bonus")
    else:
        print("Not eligible for bonus")
else:
    print("Experience criteria not met. Better luck next time :)")

# Student Scholarship

marks = 85
family_income = 250000

if marks >= 75:
    if family_income <= 100000:
        print("You are eligible for scholarship")
    else:
        print("Income is more so you are not eligible for scholarship")
else:
    print("Marks criteria do not match")

# Movie ticket discount
age = 75
is_member = True

if age >= 65:
    if is_member == True:
        print("Congratulations!! you got a senior citizen discount")
    else:
         print("Join membership to get a discount")
else:
    print("Sorry, You are not eligible for a discount")