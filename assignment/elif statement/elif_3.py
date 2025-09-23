# TODO Check the grade of a student based on marks (A, B, C, D, or Fail). 

mark = int(input("Enter your mark : "))

if mark > 90:
    print("your grade : A")
elif 80 <= mark <= 90:
    print("your grade : B")
elif 70 <= mark <= 80:
    print("your grade : C")
elif 50 <= mark <= 70:
    print("your grade : D")
else:
    print("you are Fail, but you can try to best perform")
    