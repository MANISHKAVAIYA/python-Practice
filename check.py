n = int(input("Enter the value : "))
s = str(n)

i = 0
out = ' '

while i < len(s):
    out = s[i]+out
    i+=1
out = int(out)
print(out)


