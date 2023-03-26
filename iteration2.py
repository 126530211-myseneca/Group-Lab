#!usr/bin/env python3
#author-MD Shahin Alam

'''Group Project'''

import random

#Define the option for the game
options = ["rock", "paper", "scissors"]

#Information for the player
print("Welcome to Rock, Paper, Scissors")
print("Your oponent is a computer!")

while True:
	# Computer will randomly choose an option
	ComputerChoice = random.choice(options)

	# Ask the player to make a choice
	PlayerChoice: str = input("Please choose rock, paper or scissors: ").lower()


	# To print choices of computer and the player
	print("You chose: ", PlayerChoice)
	print("The computer chose: ", ComputerChoice)

	#Checks all possible scenarios of the game based on choices
	if PlayerChoice == ComputerChoice:
			print("It's a tie!")
	elif PlayerChoice == "rock":
			if ComputerChoice != "paper":
					print("You win :)")
			else:
					print("You lose :(")
	elif PlayerChoice == "paper":
			if ComputerChoice == "scissors":
					print("You lose :(")
			else:
					print("You win :)")
	elif PlayerChoice == "scissors":
			if ComputerChoice == "rock":
					print("You lose :(")
			else:
					print("You win :)")
	else:
		print("Invalid input. Plese enter 'rock', 'paper', or 'scissors'.")
		continue

	#Ask the player if they want to play again
	PlayAgain = input("Do you want to continue playing the game? ").lower()

	# If player enter the choice 'y' then it will continue playing the game, otherwise it will exit the program
	if PlayAgain == "y":
		continue
	else: 
		print("Thanks for playing. See you next time!")
		break
