import random

name = input("Give me everybody's names, seperated by a comma.")
names= name.split(", ")
meal = random.randint(0, len(names)-1)
print(f"{names[meal]} is going to pay")
#you can use random.choice