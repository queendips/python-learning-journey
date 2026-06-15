# # Built-in functions are predefined functions that come with Python.

# len()
family_members = ["Mom" , "Dad", "sister","Me"]
print(len(family_members))

name = "India"
print(len(name))

# type()

name = "Sam"
age = 31
salary = 76965.87
skill = ["python", "jenkins","linux","docker"]
fav_colors = ("Red", "Blue", "Green")
is_indian = True
print(type(name))
print(type(age))
print(type(salary))
print(type(skill))
print(type(fav_colors))
print(type(is_indian))

# max()
marks = [67, 87, 45, 91]
print(max(marks))

print(max(98, 76, 45, 96))

fruits = ["apple", "Mango", "kiwi","orange", "Guava"]
print(max(fruits))

# min()
print(min(fruits))
print("lowest marks:", min(marks))


# sum()
expenses=[69, 50,20,10]
print(sum(expenses))

print("Highst marks : ",max(marks))
print("Lowest marks :", min(marks))
print("Total marks : ", sum(marks))

# abs()
# It returns the absolute value
print(abs(-10))
print(abs(+10))
print(abs(10.6))
print(abs(-10.6))

# round()
print(round(10.876))
print(round(95.45))
number = 7.987654
print(round(number , 3))

response_time = 123.456789

print(round(response_time, 2))