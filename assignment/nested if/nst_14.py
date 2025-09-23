# TODO 17. Check if a bank account balance is sufficient, then check if withdrawal is possible. 

bank = int(input("Enter your bank balance : "))
balance = int(input("Enter your withdrawal amount : "))

if bank > 30000:
    if balance < bank:
        print("Withdrawal is possible")
    else:
        print("not enough money in their account")
else:
    print("your bank amount is not sufficient")