# TODO Check if a given month number belongs to Winter, Summer, or Monsoon.

month = int(input("Enter the month : "))

if month in (9, 11):
    print("Monsoon") 
elif month in (1,2,3,4,5):
    print("Summer")
elif month in (6,7,8,12):
    print("Winter")
else:
    print("Invalid month")