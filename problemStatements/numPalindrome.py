num = int(input("Enter The NUmber: "))

# Convert the number to a string to check for palindrome
num_str = str(num)


# Check if the number is the same when reversed
if num_str == num_str[::-1]:
    print("The Number is palindrome: ", num_str)
else:
    print("The Number is not palindrome: ", num_str)
