# TODO 1. Check if a number is positive, then check if it's even or odd. 

value = int(input("Enter the value : "))

if value > 0:
    if value % 2 == 0:
        print("Even value")
    else:
        print("Odd value")
else:
    print("you entered negative value. try again..")