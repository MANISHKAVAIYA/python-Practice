# TODO 11. Check if an entered username is correct, then check if the password is correct. 

u = input("enter your username : ")
p = input("enter your password : ")

username = "Dwarka"
password = "Kingdom of Krishna"

if username == u:
    if password == p:
        print("Login Successfully")
    else:
        print("password is wrong")
else:
    print("check your username")