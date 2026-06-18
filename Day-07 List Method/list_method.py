fruits = ["apple", "banana", "mango"]


# append()
# Adds an item at the end of the list.
fruits.append("Orange")
print(fruits)

# insert()
# Adds an item at a specific position.
fruits.insert(2,"Kiwi")
print(fruits)

# extend()
# Adds multiple items from another list.
vegetable = ["Tomato", "chilli"]
fruits.extend(vegetable)
print(fruits)

# remove()
# Removes a specific item.
fruits.remove("chilli")
print(fruits)

# pop()
# Removes an item using its index.
fruits.pop(5)
print(fruits)
# Without an index, it removes the last item.
fruits.pop()
print(fruits)

# clear()
# Removes all items from the list.

vegetable.clear()
print(vegetable)

