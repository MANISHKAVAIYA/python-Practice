value = input("Enter the data : ")

i = 0 

u = ' '
l = ' '
n = ' '
sp = ' '

for ch in value:
    if 'A' <= ch <= 'Z':
        u += ch
    elif 'a' <= ch <= 'z':
        l += ch
    elif '0' <= ch <= '9':
        n += ch
    else:
        sp += ch

print("Uppercase : ", u)
print("lowercase : ", l)
print("Numbers : ", n)
print("Special character : ", sp)
