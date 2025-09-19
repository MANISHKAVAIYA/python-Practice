# TODO find the greatest value in four number
# !!! using the nested if 

n1 = int(input("Enter the value 1 : "))
n2 = int(input("Enter the value 2 : "))
n3 = int(input("Enter the value 3 : "))
n4 = int(input("Enter the value 4 : "))

if n1 > n2 and n1 > n3 and n1 > n4:
    print("n1 is greatest")
elif n2 > n3 and n3 > n4:
    print("n2 is greatest")
elif n3 > n4:
    print('n3 is greatest')
else:
    print("n4 is greatest")