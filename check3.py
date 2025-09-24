# TODO EXTRACTING THE CHARACTER IN UPPERCASE, LOWERCASE, NUMBERS, SPECIAL CHARACTERS

text = input("Enter a string: ")

uppercase = ""
lowercase = ""
numbers = ""
special = ""

i = 0
while i < len(text):
    ch = text[i]
    if 'A' <= ch <= 'Z':  # uppercase check
        uppercase += ch
    elif 'a' <= ch <= 'z':  # lowercase check
        lowercase += ch
    elif '0' <= ch <= '9':  # number check
        numbers += ch
    else:  # everything else = special character
        special += ch
    i += 1  # move to next character

print("Uppercase characters:", uppercase)
print("Lowercase characters:", lowercase)
print("Numbers:", numbers)
print("Special characters:", special)