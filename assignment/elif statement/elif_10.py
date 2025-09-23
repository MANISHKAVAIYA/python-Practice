# TODO 10. Check if a number is divisible by 2, 3, or neither. 

number = int(input("Enter the number : "))

if number % 2 == 0:
    print("It is divisible by 2")

elif number % 3 == 0:
    print("It is divisible by 3")

else:
    print("neither")