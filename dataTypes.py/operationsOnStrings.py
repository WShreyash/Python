"""Write a Python program to perform following operations on String.
-> Creating a String - str=" "
-> Accessing Characters in string - str[0]
-> Slicing - str[1:3]
-> Index - str.index['o']
-> Length of String - len(str)
-> lower() - str.lower()
-> upper() - str.upper()
-> capitalize() - str.capitalize
-> title() -str.title()
-> Updating a String - mutale add directly str=" "
-> Concatenating a Strings - str1+str2
-> Repeating Strings- str*3"""

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
print("Index of char:",str1.index('o'))

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
