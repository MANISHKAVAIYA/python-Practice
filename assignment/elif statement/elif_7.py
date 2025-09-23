# TODO 7. Check if a number is single-digit, double-digit, or more. 

number = int(input("Enter the number : "))

if 0 <= number < 10:
    print("entered number is single digit")
elif 10 <= number <=99:
    print("entered number is double-digit")
else:
    print("more")