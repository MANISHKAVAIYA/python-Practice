# TODO 14. Check if a given input is an alphabet, number, or special character. 

value = input("Enter the value : ")

if 'A' <= value <= 'Z' or 'a' <= value <= 'z':
    print("alphabet")

elif '0' <= value <= '9':
    print("number")

else:
    print("Special Character")