# TODO Check if a triangle is valid based on the sum of its angles. 

value1 = int(input("Enter the angle 1 : "))
value2 = int(input("Enter the angle 2 : "))
value3 = int(input("Enter the angle 3 : "))



if value1+value2+value3 == 180:
    print("This is a triangle")

else:
    print("It is not triangle")