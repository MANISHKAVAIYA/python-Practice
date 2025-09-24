ab = "Python is Easy @12$"

#special = ''

u = []
l = []
n = []
s = []

i = 0
while i < len(ab):
    store = ab[i]
    if "A" <= store <= "Z":
        u += store
    elif 'a' <= store <= 'z':
        l += store
    elif '0' <= store <= '9':
        n += store
    else:
        s += store
    i += 1

print("uppercase : ", u)
print('lowercase : ', l)
print('numbers : ', n)
print('special character : ', s)