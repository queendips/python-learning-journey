import math
#sqrt
print(math.sqrt(25))
#pow
print(math.pow(2, 3))
#pi
print(math.pi) #alue of π
#factorial
print(math.factorial(5))
print(math.factorial(0))
#ceil
# The ceil() function returns the smallest integer greater than or equal to the given number.

# Think of it as always rounding upward.
print(math.ceil(4.2))
print(math.ceil(7.6))
print(math.ceil(-2.1))

#floor
print(math.floor(4.9))
print(math.floor(99 / 20))
#fbs()
# The fabs() function returns the absolute (positive) value of a number as a float.
print(math.fabs(15))
#abs
print(abs(-5))
#e
# math.e returns Euler's number, approximately 2.71828.
print(math.e)
# sin(), cos(), tan()
# The math module's trigonometric functions expect angles in radians, so math.radians() converts degrees into radians before calculation.
angle = math.radians(30)

print(math.sin(angle))
print(math.cos(angle))
print(math.tan(angle))
#log
# The log() function returns the natural logarithm (base e) of a number.
print(math.log(10))
