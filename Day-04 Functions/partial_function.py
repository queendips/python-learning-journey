# A Partial Function is a new function created by fixing one or more arguments of an existing function.
# Python provides this through the functools module.
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)

print("Double of 5:", double(5))
print("Double of 10:", double(10))
print("Double of 20:", double(20))

#--------------------
def calculate_shipping(base_charge, weight):
    return base_charge * weight

fast_shipping = partial(calculate_shipping, 50)

print("Shipping Cost:", fast_shipping(2))
print("Shipping Cost:", fast_shipping(5))