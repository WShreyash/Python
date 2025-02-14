# perfet num = sum of all its divisors is equal to that num
num = int(input("Enter The Num: "))

sum_of_divisors = 0

for i in range(1, (num//2) + 1):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print("Number", num, "Is A perfect Number")
else:
    print("Number", num, "Is not a perfect Number")
