# TODO 8. Check if a person’s weight category is underweight, normal, or overweight. 

weight = int(input("Enter your weight : "))

if weight >= 80:
    print("overweight")

elif 50 <= weight <= 80:
    print("normal")

elif 40 <= weight <= 50:
    print("underweight")

else:
    print("you are lucky to archive your weight")