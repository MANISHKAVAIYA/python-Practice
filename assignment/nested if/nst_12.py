# TODO 12. Check if a triangle is valid, then check if it's equilateral, isosceles, or scalene. 

# using gpt


angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

# Check if triangle is valid
if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    # Nested if to classify
    if angle1 == angle2 == angle3:
        print("Equilateral triangle")
    else:
        if angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
else:
    print("Invalid triangle")
