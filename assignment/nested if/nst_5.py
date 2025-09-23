# TODO 5. Check if a given character is an alphabet, then check if it's uppercase or lowercase.

character = input("Enter any character : ")

if len(character) == 1:
    if character.isalpha:
        if character == character.upper():
            print("The character is uppercase")
        else:
            print("lowercase")
    else:
        print("Not alpha value")
else:
    print("Entered value is not allowed")