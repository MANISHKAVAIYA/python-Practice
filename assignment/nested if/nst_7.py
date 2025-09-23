# TODO 7. Check if a year is a leap year, then check if it is a century year. 

# using gpt

year = int(input("Enter a year: "))

if year <= 0:
    print("Invalid year")
else:
    # Check leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is a common year")
    
    # Check century year
    if year % 100 == 0:
        print(f"{year} is a century year")
    else:
        print(f"{year} is not a century year")
