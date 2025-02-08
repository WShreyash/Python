"""Write a Python program to perform following operations on String.
-> Creating a String
-> Accessing Characters in string
-> Slicing
-> Index
-> Length of String
-> lower()
-> upper()
-> capitalize()
-> title()
-> Updating a String
-> Concatenating a Strings
-> Repeating Strings"""

# Creating a String
str1 = "Hello, World!"
print("Created String:", str1)

# Accessing Characters in String
print("First Character:", str1[0])
print("Last Character:", str1[-1])

# Slicing
print("Sliced String (0:5):", str1[0:5])

# Index
print("Character at Index 7:", str1[7])

# Length of String
print("Length of String:", len(str1))

# String Methods
print("Lowercase:", str1.lower())
print("Uppercase:", str1.upper())
print("Capitalize:", str1.capitalize())
print("Title Case:", str1.title())

# Updating a String (Strings are immutable, so we create a new one)
str1 = "Hello, Python!"
print("Updated String:", str1)

# Concatenating Strings
str2 = " Let's learn Python."
print("Concatenated String:", str1 + str2)

# Repeating Strings
print("Repeated String:", str1 * 3)
