# TODO Check if a person is eligible for a senior citizen discount (age >= 60). 

n = int(input("Enter your age : "))

discount = "discount eligible"

if n >= 60:
    print("you are senior citizen", discount)

else:
    print("you are not eligible")