from art import logo
import os

print(logo)
print("Welcome to the secret auction program.\n")

newdic = {}
play= True
while play == True:
    name =input("What is your name ")
    bid = int(input("What is your bid? $"))

    #newdic ={}  this is a mistake, reinitializing the dictionary in every loop
    newdic[name]= bid
    
    keyz = 0
    for key in newdic:
        if keyz < newdic[key]:
            keyz = newdic[key]
            winner = key

    result = input("Are there any other bidders? 'Yes' or 'No'.\n").lower()
    if result == "no":
        play= False
        print(f"The winner is {winner} with a bid of {keyz}")
    elif result == "yes":
        os.system('cls') #for windows