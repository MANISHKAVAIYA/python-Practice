# TODO EXTRACTING THE CHARACTER IN UPPERCASE, LOWERCASE, NUMBERS, SPECIAL CHARACTERS

a = "Python@123!9"
out = 0

upper = []
lower = []
number = []
special_char = []

while out<len(a) :
    if 'A'<= a[out]<= 'Z':
        print("uppercase")
    elif 'a' <= a[out] <= 'z':
        print("lowercase")
    elif '0' <= a[out] <= '9':
        print("numbers")
    else:
        print("special character")
    out+=1
print(upper)