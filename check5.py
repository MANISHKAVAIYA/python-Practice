a='PYtHon@#123'

u = ''
l = ''
d = ''
sc = ''

i=0
while i<len(a):
    if 'A'<=a[i]<='Z':
        u+=a[i]
    elif 'a'<=a[i]<='z':
        l+=a[i]
    elif '0' <=a[i] <='9':
        d+=a[i]
    else:
        sc+=a[i]
    i+=1


print("uppercase : ", u)
print("lowercase : ", l)
print("number : ", d)
print("special character : ", sc)
