# TODO 16. Check if a product is in stock, then check if it is on sale. 

value = int(input("Enter stocks : "))
sale = input("choose a sale product : ")
products = ['samsung', 'apple']

if value > 0:
    if sale in products:
        print("Yes, this product is offer in sale")
    else:
        print("not sale in this chosen product")
else:
    print("stock is unavailable")