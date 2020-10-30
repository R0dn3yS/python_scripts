import json

caesar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
alphabet = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', ' ']
converted = ""

def convertCaesar(w, c):
    for letter in w:
        position = alphabet.index(letter, 0, 27)
        c = c + caesar[position]
    return c

def convertBack(w, c):
    for letter in w:
        position = caesar.index(letter, 0, 27)
        c = c + alphabet[position]
    return c

def option():
    choice = input("Choose an option: \n1. Convert to Caesar \n2. Convert back\n")
    if choice == "1":
        word = input("Word to convert: ").lower()
        print(convertCaesar(word, converted))
        convertedWord = convertCaesar(word, converted)
        f=open("cypher.txt", "a")
        f.write('Original: ' + word + ', ' 'Converted: ' + convertedWord)
        f.close()
    elif choice == "2":
        word = input("Word to convert: ").lower()
        print(convertBack(word, converted))
        convertedWord = convertBack(word, converted)
        f=open("cypher.txt", "a")
        f.write('Original: ' + word + ', ' 'Converted: ' + convertedWord)
        f.close()
    else:
        option()

option()