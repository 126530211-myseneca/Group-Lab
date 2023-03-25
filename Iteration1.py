#! usr/bin/env python3
# Author-Taranjot Kaur

'''Group Project'''

import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors")
print("Your oponent is a computer!")

# Computer will randomly choose an option
ComputerOption = random.choice(options)

# Ask the player to make a choice
PlayerOption = input("Please choose rock, paper or scissors: ").lower()


# To print choices of computer and the player
print("You chose: ", PlayerOption)
print(f"The computer chose: ", ComputerOption)


# To check the validation of player's choice
#if PlayerOption not in options:
#      print("Invalid Choice! Please try again!")
 #     continue

# Decides the winner
if PlayerOption == ComputerOption:
        print("It's a tie!")
elif PlayerOption == "rock":
        if ComputerOption == "paper":
                print("You lose :(")
        else:
                print("You win :)")
elif PlayerOption == "paper":
        if ComputerOption == "scissors":
                print("You lose :(")
        else:
                print("You win :)")
elif PlayerOption == "scissors":
        if ComputerOption == "rock":
                print("You lose :(")
        else:
                print("You win :)")
else:
        print("Invalid input. Plese enter 'rock', 'paper', or 'scissors'.")

print("Thanks for playing. See you next time!")

