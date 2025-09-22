age = int(input("Enter your age : "))
experience = int(input("Enter your experience : "))

if age >= 18:
    if experience >= 2:
        print("You are selected to our company")
    else:
        print("you have not enough experience")
else:
    print("you are not eligible")