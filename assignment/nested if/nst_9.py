# TODO 9. Check if a number is positive, then check if it’s a prime number.

# using gpt 

value = int(input("Enter the value: "))

if value > 0:  # positive check
    if value == 1:
        print("1 is not a prime number")
    else:
        if value == 2:
            print("2 is a prime number")
        else:
            if value == 3:
                print("3 is a prime number")
            else:
                if value == 4 or value == 6 or value == 8 or value == 9 or value == 10:
                    print(f"{value} is not a prime number")
                else:
                    print(f"{value} is a prime number")
else:
    print("Not a positive number")
