
print("Welcome to the ROCK, PAPER, SCISSORS game!!!\n")
print("These are the rules of the game:\n"
       "Rock breaks Scissors\n"
       "Scisors cuts Paper\n"
       "Paper covers the Rock\n")

rounds = 0

import random

while True:
    ComputerChoice =  random.choice(["rock", "paper", "scissors"])
    UserChoice = input("Choose ROCK, PAPER, OR SCISSORS: ")
    print("UserChoice:", UserChoice, "\nComputerChoice:", ComputerChoice)

    if ComputerChoice == UserChoice:
        print("This is a tie, choose again.")
        UserChoice = input("Choose ROCK, PAPER, OR SCISSORS ")

    elif ComputerChoice == "rock":
        if UserChoice == "paper":
            print("You Win!")
        else:
            print("You Loose!")

    elif ComputerChoice == "paper":
        if UserChoice == "scissors":

            print("You Win!")
        else:
            print("You Loose!")

    elif ComputerChoice == "scissors":
        if UserChoice == "rock":
            print("You Win!")
        else:
            print("You Loose!")

    rounds += 1
    if rounds == 2:
        break

