# TODO 8. Check if a person is eligible for a discount, then check if the purchase is above 10,000. 

print("amount should enter only two-digits")

Value = int(input("Enter the amount : "))

if Value > 10:
    if Value > 25:
        print(f"your amount {Value}K is eligible for discount")
    else:
        print(f"your amount {Value}K is not eligible for discount")
else:
    print("your purchase amount is not above 10K")