import random
#random
print(random.random())
#randint()
print(random.randint(1, 10))
#randrange()
# Returns a random number from a specified range.
# Syntax: random.randrange(start, stop, step)
print(random.randrange(0, 20, 2))
#uniform
# Returns a random floating-point number between two numbers.
#syntax: random.uniform(start, end)
print(random.uniform(1,7))
#choice()
#The choice() function returns one random element from a sequence such as a list, tuple, or string.
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(random.choice(fruits))
print(random.choice("PYTHON"))

#choices
# The choices() function returns multiple random elements from a sequence.
# By default, it allows duplicates (sampling with replacement).
print(random.choices(fruits, k=3))

#sample()
# The sample() function returns multiple unique random elements from a sequence.
# It does not allow duplicates (sampling without replacement).
print(random.sample(fruits, 3))
#shuffle()
#The shuffle() function randomly rearranges the elements of a list.
# It modifies the original list and returns None.
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)

#seed()
# The seed() function initializes the random number generator with a fixed value, making the sequence repeatable.
random.seed(10)

print(random.randint(1, 100))
print(random.randint(1, 100))
#getrandbits()
# Returns a random integer with the specified number of binary bits.
# Used in cryptography and generating random binary values.
#syntax:random.getrandbits(bits)
print(random.getrandbits(4))
#randbytes()
# Returns a specified number of random bytes.

# Syntax : random.randbytes(n)
print(random.randbytes(5))
# triangular
# Returns a random floating-point number following a triangular distribution.
#syntax:random.triangular(low, high, mode)
print(random.triangular(10, 20, 15))
#betavariate()
# Returns a random floating-point number following a Beta distribution.
#syntax:random.betavariate(alpha, beta)
print(random.betavariate(2, 5))
#expovariate()
# Returns a random number following an Exponential distribution.
#syntax:random.expovariate(lambda_value)
print(random.expovariate(1))
# gauss()
# Returns a random number from a Gaussian (Normal) distribution.
#syntax:random.gauss(mean, standard_deviation)
print(random.gauss(50, 10))

# normalvariate()

# Works similarly to gauss() and returns a value from a normal distribution.
print(random.normalvariate(100, 15))
# vonmisesvariate()
# Returns a random angle using the Von Mises distribution.
print(random.vonmisesvariate(0, 4))