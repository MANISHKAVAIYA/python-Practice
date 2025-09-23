# TODO 15. Check if a year is Leap, Common, or Invalid. 

# using gpt

year = int(input("Enter a year: "))

if year <= 0:
    print("Invalid year")
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Common year")
