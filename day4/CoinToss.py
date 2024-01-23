import random

Toss = input("Heads or Tails? ")

random_side = random.randint(0, 1)
if random_side == 1 and Toss == "Heads":
    print("Heads!\nYou win!")
elif random_side == 0 and Toss == "Tails":
    print("Tails!\nYou win!")
else:
    print("You lose :)")