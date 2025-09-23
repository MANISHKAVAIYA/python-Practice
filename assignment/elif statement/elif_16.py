# TODO  Check if a train ticket is Economy, Business, or First Class.

print("1. Economy Ticket")
print("2. Business Ticket")
print("3. First Class")

ticket = input("Enter your ticket : ")

if ticket in ('Economy','economy'):
    print("Your ticket is economy")

elif ticket in ('Business', 'business'):
    print("Your ticket is business")

elif ticket in ('First Class', 'first class', 'firstclass'):
    print("Your ticket is first class")

else:
    print("try again")