# TODO 18. Check if an email is valid, then check if it contains a certain domain. 

mail = input("Enter your email : ")
select_dm = input("Enter your domail : ")
domain = ['tech', 'com', 'education', 'business', 'hospital']

if '@' in mail or '0' <= mail <= '9' and 'mail' in mail:
    if select_dm in domain:
        if '@tech' in mail or '@business' in mail or '@edu' in mail or '@gmail' in mail:
            print('you are in certain domain')
        else:
            print("you are not certain domain")
    else:
        ('check again your domain')
else:
    print("Not valid email")
