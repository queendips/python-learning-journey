# calendar.month(year, month)
import calendar
print(calendar.month(2026, 7))
print(calendar.calendar(2026))
#calendar.isleap(year)
print(calendar.isleap(2024)) #Checks whether a year is a leap year. 
# calendar.weekday()
# calendar.weekday(year, month, day)
# Returns the day of the week as a number.
print(calendar.weekday(2026, 7, 25))

# calendar.monthrange()
# Returns:
# First weekday of the month
# Number of days in that month
# Syntax: calendar.monthrange(year, month)

print(calendar.monthrange(2026, 7))

# calendar.month_name
for month in calendar.month_name:
    print(month)

# calendar.day_name
for day in calendar.day_name:
    print(day)