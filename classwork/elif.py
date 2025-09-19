a = eval(input("enter the value : "))

if a == int(a) or a == float(a) or a == complex(a) or a == bool(a):
    print("single value")

else:
    print("Not Single Value")

#  print("Everytime executes")


# !! second method

if type(a) in [int, float, complex, bool]:
    print('Single Value Data Type')

else:
    print('Multi Value Data type')