"""Write a Python program to perform following operations on Dictionary.
-> Creating a Dictionary
-> Accessing a Dictionary
-> Ordered
-> Adding Elements
-> Removing Elements
-> Duplicate
-> Accessing Keys
-> Accessing Values
-> Index
-> Dictionary Length
-> Dictionary Items - Data Types"""

# Creating a Dictionary
dict1 = {"name": "Shreyash", "age": 18, "city": "New York"}
print("Created Dictionary:", dict1)

# Accessing a Dictionary
print("Accessing 'name':", dict1["name"])

# Ordered (Since Python 3.7+, dictionaries maintain insertion order)
dict1["country"] = "USA"
print("Dictionary after adding 'country':", dict1)

# Adding Elements
dict1["job"] = "Engineer"
print("Dictionary after adding 'job':", dict1)

# Removing Elements
del dict1["age"]
print("Dictionary after removing 'age':", dict1)

# Duplicate Keys (Keys must be unique, last value will overwrite previous ones)
dict1["name"] = "Bob"
print("Dictionary after duplicate key update:", dict1)

# Accessing Keys
keys = dict1.keys()
print("Dictionary Keys:", list(keys))

# Accessing Values
values = dict1.values()
print("Dictionary Values:", list(values))

# Index (Dictionaries do not have a numeric index like lists, but keys work as indexes)
key_list = list(dict1.keys())
print("Accessing by index [1]:", dict1[key_list[1]])

# Dictionary Length
print("Dictionary Length:", len(dict1))

# Dictionary Items - Data Types
print("Dictionary Items and Data Types:")
for key, value in dict1.items():
    print(f"{key}: {value} ({type(value)})")
