# TODO 12. Check if a triangle is Equilateral, Isosceles, or Scalene. 

# Equilateral: All three sides are equal (a == b == c).

# Isosceles: Exactly two sides are equal (a == b or b == c or a == c).

# Scalene: All sides are different (a != b != c != a).

angle1 = int(input("Enter the value 1 : "))
angle2 = int(input("Enter the value 2 : "))
angle3 = int(input("Enter the value 3 : "))

if angle1 == angle2 == angle3:
    print("Equilateral")

elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
    print("isosceles")

elif angle1 != angle2 != angle3 != angle1:
    print("Scalene")

else:
    print("Invalid Value")