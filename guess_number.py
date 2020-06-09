from random import randint
from pyfiglet import figlet_format
from termcolor import cprint

# Overview:
# The computer randomly generates a number. The user inputs a number, and the computer will tell you if you are too high, or too low. Then you will get to keep guessing until you guess the number.
#print game header
header = cprint(figlet_format("Number Guesser", font="slant"), color="blue")
#generate number based on user provided rannge
guessing_range = int(input("Please provide a number: "))

print("The computer will now select a number at random, how many guesses will it take you to determine the correct number? ")

secret_num = randint(1, guessing_range)

guess = None
number_of_guesses = 0

def guess_protocol(num):
	if guess > secret_num:
		print ("Oops, too high, try again")
	elif guess < secret_num:
		print ("Oops, too low, try again")
		

while guess != secret_num:
	if guess is None:
		guess = int(input("Provide your first guess: "))
		guess_protocol(guess)
		number_of_guesses += 1
	else:
		guess = int(input("Provide your next guess: "))
		guess_protocol(guess)
		number_of_guesses += 1

print(f"Congrats, you guessed it! The number was {secret_num}!\nIt took you {number_of_guesses} tries \U0001f600" + ("\n" *5))
game_over = cprint(figlet_format("GAME OVER"), color="magenta")
 