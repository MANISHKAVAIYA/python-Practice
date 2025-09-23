# TODO 4. Check if a number is greater than 50, then check if it's divisible by 10. 

value = int(input("Enter the value : "))

if value > 50:
    if value % 10 == 0:
        print(f"The {value} is divisible by 10 ")
    else:
        print("Not divisible")
else:
    print("Value is not greater than 50")
