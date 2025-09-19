u = 'Dwarka'
p = 'Kingdom of Krishna'

username = input("Enter the username : ")
password = input("Enter the password : ")

if u == username:
    if p == password:
        print("Login successfully")
    else:
        print("Invalid password")
else:
    print('Invalid username')
