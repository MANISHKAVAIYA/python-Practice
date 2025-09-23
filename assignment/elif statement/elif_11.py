# TODO 11. Check if an employee’s salary falls into Low (<30K), Medium (30K-60K), or High (>60K). 

print("salary must entered in double-digit only")
sal = int(input("Enter your salary : "))

if sal < 30:
    print(f"your salary {sal}K is low")

elif 30 <= sal <= 60:
    print(f"your salary {sal}K is Medium")

elif sal > 60:
    print(f"your salary {sal}K is High")

else:
    print("you are fresher or intern")