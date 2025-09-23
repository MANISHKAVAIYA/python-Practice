# TODO 9. Check if an input character is a vowel, consonant, or other symbol. 

alpha = input("Enter the character : ")

if alpha in 'aeiouAEIOU':
    print("Vowel")

elif alpha not in 'aeiouAEIOU':
    print("consonant")

else:
    print("other symbol")