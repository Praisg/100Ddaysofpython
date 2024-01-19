print("Welcome to the Love calculator")
name1 = input("What is your name ?\n")
name2 = input("What is their name?\n")

name = (name1+name2).lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = t+r+u+e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
love = l+o+v+e

loveScore1 = str(true)+str(love)
loveScore = int(loveScore1)
if loveScore<10 or loveScore>90:
    print(f"Your score is {loveScore}, You go together like coke and mentos ")
elif loveScore>=40 & loveScore<=50:
    print(f"Your score is {loveScore}, you are alright together")
else:
    print(f"Your score is{loveScore}")    
        