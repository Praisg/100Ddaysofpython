from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

play = True
while play == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(text,shift):
        word =""
        if direction == "decode":
            shift *= -1

        for x in text:  #iterate thru the word first :lesson 1
            if x in alphabet:
                new = (alphabet.index(x) + shift)%26
                word += alphabet[new]
            else:
                word += x      
        print(f"The encrypted word is {word}\n")


    if direction == "encode" or direction == "decode" :
        encrypt(text,shift)
    else:
        print("Invalid Option! Specify if you want to encrypt or decrypt")

    result = input("Type 'Yes' if you wnat to go again. Otherwise type 'No'\n ").lower()
    if result == 'no':
        play = False
        print("Goodbye :( ")

