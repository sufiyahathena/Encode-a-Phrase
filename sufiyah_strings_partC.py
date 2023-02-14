#SUFIYAH SAJAN
#Strings Assignment
#Part C

import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def add_letters(string, number):
    string = list(string)
    encodelist = []
    for letter in range(0, len(string)):
        encodelist.append(string[letter])
        for x in range(0, number):
            encodelist.append(random.choice(letters))
    return encodelist

def remove_letters(string, number):
    string = list(string)
    decodelist = []
    for letter in range(0, len(string), number +1):
        decodelist.append(string[letter])
    return decodelist

def shift_characters(string, number):
    string = list(string)
    shiftlist = []
    for char in range(0,len(string)):
        shiftlist.append(chr(ord((string[char])) + number))
    return shiftlist

cont = input("Either encode (e), decode (d) or quit (q): ")

while cont == 'e' or 'd':
    if cont == 'q':
        break
    elif cont == 'd':
        numb = input("Enter a number between 1 and 5: ")
        phrase = input("Enter a phrase to encode: ")
        encode3 = remove_letters(phrase, int(numb))
        encode4 = shift_characters(encode3, -abs(int(numb)))
        print("Your decoded word is: ", ''.join(encode4))
        print()
        cont = input("Either encode (e), decode (d) or quit (q): ")
    elif cont == 'e':
        numb = input("Enter a number between 1 and 5: ")
        phrase = input("Enter a phrase to encode: ")
        encode1 = add_letters(phrase, int(numb))
        encode2 = shift_characters(encode1, int(numb))
        print("Your encoded word is: ", ''.join(encode2))
        print()
        cont = input("Either encode (e), decode (d) or quit (q): ")
    
