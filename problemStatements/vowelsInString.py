text = input("Enter The String: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1

print("The Number vowels in a string are ", count)
