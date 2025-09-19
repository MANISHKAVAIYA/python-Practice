# TODO USING GREATEST THREE NUMBER NESTED IF

n1 = int(input("Enter the value 1 : "))
n2 = int(input("Enter the value 2 : "))
n3 = int(input("Enter the value 3 : "))

if n1 > n2:
    if n1 > n3:
        print("n1 is greatest")

    else:
        print("n3 greatest")
else:
    if n2 > n3:
        print("n2 is greatest")
    else:
        print("n3 greatest")
        