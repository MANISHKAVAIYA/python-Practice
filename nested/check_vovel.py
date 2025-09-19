a = input('Enter the character: ')

if len(a) == 1:
    if 'A'<=a<='Z' or 'a'<=a<='z':
            if a in 'AEIOUaeiou':
                print('It is vowel')
            else:
                print('It is consonant')
    else:
       print('Give only uppercase or lowercase characters')
else:
     print('Give only single character')

    