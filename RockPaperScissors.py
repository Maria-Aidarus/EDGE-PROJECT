print("Welcome to the ROCK, PAPER, SCISSORS game!!!\n")
print("These are the rules of the game:\n"
       "Rock breaks Scissors\n"
       "Scisors cuts Paper\n"
       "Paper covers the Rock\n")
print("In order to win this game you must win atleast two out of the three rounds.\n")

import random

x = 0
UserCounter = 0
ComputerCounter = 0


for x in range(3):

    ComputerChoice =  random.choice(["rock", "paper", "scissors"])
    UserChoice = input("Choose ROCK, PAPER, OR SCISSORS:")
    print("\nUserChoice:", UserChoice, "\nComputerChoice:", ComputerChoice, "\n")

    # while UserChoice != "rock" or UserChoice != "paper" or UserChoice != "scissors":
    #     AskAgain = input("Choose a valid input: choose ROCK, PAPER, OR SCISSORS:")

    if ComputerChoice == UserChoice:
        print("This is a tie.")

    elif ComputerChoice == "rock":
        if UserChoice == "paper":
            print("You won this round!","\U0001f600")
            UserCounter += 1
        else:
            print("You lost this round.", "\U0001F612")
            ComputerCounter += 1

    elif ComputerChoice == "paper":
        if UserChoice == "scissors":
            print("You won this round!","\U0001f600")
            UserCounter += 1
        else:
            print("You lost this round.", "\U0001F612")
            ComputerCounter += 1

    elif ComputerChoice == "scissors":
        if UserChoice == "rock":
            print("You won this round!","\U0001f600")
            UserCounter += 1
        else:
            print("You lost this round.", "\U0001F612")
            ComputerCounter += 1


print("\nComputerCounter:", ComputerCounter, "\nUserCounter:", UserCounter)

if UserCounter >= 2:
    print("You WON the Game!", "U0001F389")
elif ComputerCounter >= 2:
    print("You lost the game.")
elif ComputerCounter == 0 or 1 and UserCounter == 0 or 1:
    print("Nobody has won this game")


