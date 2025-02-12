num = int(input("Enter The Number: "))
if num > 1:

    # Iterates from 2 to n // 2
    for i in range(2, (num//2)+1):

        if (num % i) == 0:
            # If divisors were found, it's not prime
            print(num, "is not a prime number")
            break
    else:
        # If no divisors were found, it's prime
        print(num, "is a prime number")
else:
    # If num is less than or equal to 1, it's not prime
    print(num, "is not a prime number")
