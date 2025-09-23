# TODO 3. Check if a person is eligible to vote, then check if they are a senior citizen. 

age = int(input("Enter your age : "))

if age > 18:
    if age > 60:
        print("You are a senior citizen")
    else:
        print("not senior citizen")
else:
    print("you are not eligible for vote")