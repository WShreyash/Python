"""Write a Python program to perform following operations on Set.
-> Creating a Set
-> Accessing Elements
-> Index - not possible as sets are unordered
-> Slicing - not possible as sets are unordered
-> Order - not possible as sets are unordered
-> Adding Elements 
-> Removing Elements 
-> Duplicate - not allowed
-> Changeable elements"""

# Creating a Set
set1 = {"apple", "banana", "cherry"}
print("Created Set:", set1)

# Accessing Elements (Using a loop since direct indexing is not possible)
print("Accessing Elements:")
for item in set1:
    print(item)

# Index - Not possible as sets are unordered
# Slicing - Not possible as sets are unordered
# Order - Not possible as sets are unordered

# Adding Elements
set1.add("orange")
print("Set after adding 'orange':", set1)

# Removing Elements
set1.remove("banana")  # Raises KeyError if the element does not exist
print("Set after removing 'banana':", set1)

# Duplicate - Not allowed (duplicates are automatically removed)
set1.add("apple")  # No effect as "apple" is already present
print("Set after adding duplicate 'apple':", set1)

# Changeable elements (Sets do not allow mutable elements like lists)
# Example of an invalid operation:
# set1.add([1, 2, 3])  # TypeError: unhashable type: 'list'

print("Final Set:", set1)
