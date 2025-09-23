n=int(input("enter:"))
out=0
while n!=0:
    ld=n%10
    out=out*10+ld
    n=n//10
    print(out)