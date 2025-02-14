num = int(input("Enter a number: "))

# Convert number to string to determine the number of digits
num_digits = len(str(num))
sum_of_powers = 0
temp = num 

# Loop through each digit
while temp > 0:
    digit = temp % 10  # Extract last digit
    sum_of_powers += digit ** num_digits  # Raise to the power of total digits and add to sum
    temp //= 10  # Remove last digit

if sum_of_powers == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")

