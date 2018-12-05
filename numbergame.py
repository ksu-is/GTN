#this is a number game where you guess the number. You get seven guesses to figure out a number between 1 and 50.
import random

#this is letting youu the numbers are between 1 and 50.
numberofGuesses = 0
number = random.randint(1,50)

name = input("Hello! What is your name? ")

print(name + ", I am thinking of a whole number between 1 and 50. Can you guess what it is?")

while numberofGuesses < 8: 
	guess = input("Take a guess ")
	guess = int(guess)

	numberofGuesses = numberofGuesses + 1;
	guessesLeft = 8 - numberofGuesses;

#this lets you know how many guesses you have left and if you were too low.
	if guess < number:
		guessesLeft=str(guessesLeft)
		print("Your guess is too low! You have " + guessesLeft + " guesses left")

#this lets you know if you were too high and how many guesses you have left.
	if guess > number:
		guessesLeft=str(guessesLeft)
		print("Your guess is too high! You have " + guessesLeft + " guesses left")

	if guess==number:
		break

#this lets you know that you guessed correctly and tell you how many guesses you used.
if guess==number:
	numberofGuesses=str(numberofGuesses)
	print("Good job! You guessed the number in " + numberofGuesses + " tries :)")

#this lets you know that you did not guess the number correctly in seven tries and it tells you what the number is.
if guess!=number:
	number=str(number)
	print("Sorry. The number I was thinking of was " + number + " :)")
