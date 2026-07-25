# The statistics module is a built-in Python module used to perform basic statistical calculations on numerical data.
# mean()
# Mean = Sum of all numbers / Total number of values
# syntax: statistics.mean(data)
import statistics

marks = [80, 90, 75, 85, 95]

print(statistics.mean(marks))

# median()
# Returns the middle value after sorting the data.
# Syntax
# statistics.median(data)
# numbers = [10, 30, 20, 50, 40]
numbers = [10, 20, 30, 40]
print(statistics.median(numbers))
# mode
# Returns the most frequently occurring value.
numbers = [1, 2, 2, 3, 4, 2, 5]

print(statistics.mode(numbers))

# stdev()
# Standard deviation tells you how spread out the values are from the average.

# Small standard deviation → Values are close to the mean.
# Large standard deviation → Values are more spread out.
numbers = [10, 20, 30, 40, 50]
print(statistics.stdev(numbers))
# variance()
# Returns the variance of a dataset.
# Variance measures how far each value is from the mean.
numbers = [10, 20, 30, 40, 50]
print(statistics.variance(numbers))