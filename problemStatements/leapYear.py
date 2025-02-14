year = int(input("Enter The Year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is the leap year")
else:
    print(f"The year {year} is not leap year")
