# import datetime
# datetime.datetime.now()
# from datetime import datetime
# datetime.now()
import datetime
current = datetime.datetime.now()
print(current)

#--------------------------------
from datetime import datetime

now = datetime.now()

print("Year :", now.year)
print("Month:", now.month)
print("Day  :", now.day)
print("Hour :", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# strftime()
# strftime() converts a date or datetime object into a formatted string.
# datetime.strftime(format)
print(now.strftime("%d-%m-%Y"))

print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%I:%M:%S %p"))

# strptime()
# strptime() converts a string into a datetime object.
#syntax: datetime.strptime(date_string, format)
date_string = "23-07-2026"
date_object = datetime.strptime(date_string, "%d-%m-%Y")
print(date_object)

# timedelta()
# timedelta represents the difference between two dates or times.
#Add Days
from datetime import timedelta
today = datetime.now()
future = today + timedelta(days=10)
print(future)
#Subtract Days
from datetime import datetime, timedelta
today = datetime.now()
past = today - timedelta(days=5)
print(past)

# Creating Custom Date & Time Objects
from datetime import date
birthday = date(1990, 10, 15)
print(birthday)

# Create a Date and Time
from datetime import datetime
meeting = datetime(2026, 8, 1, 10, 30, 0)
print(meeting)	