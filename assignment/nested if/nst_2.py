# TODO 2. Check if a number is negative, then check if it's a multiple of 5. 

value = int(input("Enter the value : "))

if value < 0:
    if value % 5 == 0:
        print(f"value multiple by 5 ")
    else:
        print("Try again..")
else:
    print("this is a positive value")