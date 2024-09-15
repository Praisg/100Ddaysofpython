import random

num = random.randint(1, 100)

print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
level = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
	attempts = 10
	print(f"You have {attempts} attempts remaining")
elif level == "hard":
	attempts = 5
	print(f"You have {attempts} attempts remaining")
else:
	print("Invalid input")
	attempts = 0

def game(attempts):
	while attempts > 0:
		guess = int(input("Make a guess: "))
		if guess == num:
			print("You guessed the correct number")
			return
		elif guess < num:
			attempts -= 1
			print(f"Too low\nYou have {attempts} attempts remaining")
		elif guess > num:
			attempts -= 1
			print(f"Too high\nYou have {attempts} attempts remaining")
	
	if attempts == 0:
		print(f"You have lost. The correct answer is {num}")

if attempts > 0:
	game(attempts)