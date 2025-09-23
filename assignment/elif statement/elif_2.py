# TODO 2. Check if a person is a child (age < 13), teenager (13-19), or adult (20+). 

n  = int(input("Enter your age : "))

if n < 13:
    print("you are child")
elif 13<=n<=19:
    print("you are teenager")
elif n > 20:
    print("you are adult")
else:
    print("you are older")