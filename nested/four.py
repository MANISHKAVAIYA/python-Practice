# TODO write a program to check whether a given number is double digit or not then check if it is divisible by 4 or not


a = input("Enter the value 1 : ")
# b = input("Enter the value 2 : ")

if len(a) == 2:
    if a % 4 == 0:
        print('divisible by four')
    else:
        print("not divisible by four and not")
else:
    print("not valid").