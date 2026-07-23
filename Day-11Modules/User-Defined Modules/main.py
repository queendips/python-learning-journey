import area

print("Square Area:", area.square(5))
print("Rectangle Area:", area.rectangle(10, 4))

# ---------
# Imports only specific function(s)
from calculator import add, multiply

print(add(10, 20))
print(multiply(5, 6))
# --------------------
# import module as alias
import calculator as cal

print(cal.add(10, 20))
print(cal.multiply(5, 6))

# from module import *
from calculator import *

print(add(10, 20))
print(subtract(50, 30))
print(multiply(5, 6))