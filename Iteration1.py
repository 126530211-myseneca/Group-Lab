#! usr/bin/env python3
# Author-Taranjot Kaur

'''Group Project'''

import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors")
print("Your oponent is a computer!")

# Computer will randomly choose an option
ComputerChoice = random.choice(options)

# Ask the player to make a choice
PlayerChoice = input("Please choose rock, paper or scissors: ").lower()


# To print choices of computer and the player
print("You chose: ", PlayerChoice)
print("The computer chose: ", ComputerChoice)

# Decides the winner
if PlayerChoice == ComputerChoice:
        print("It's a tie!")
elif PlayerChoice == "rock":
        if ComputerChoice == "paper":
                print("You lose :(")
        else:
                print("You win :)")
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

print("Thanks for playing. See you next time!")

