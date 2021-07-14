
print("Welcome to the ROCK, PAPER, SCISSORS game!!!\n")
print("These are the rules of the game:\n"
       "Rock breaks Scissors\n"
       "Scisors cuts Paper\n"
       "Paper covers the Rock\n")
print("In order to win this game you must win atleast two out of the three rounds.\n")


# rounds = 0

import random     #Imports a random choice

# while True:
x = 0
UserCounter = 0
ComputerCounter = 0

# while x < 3:
for x in range(3):   #Runs for three rounds

    ComputerChoice =  random.choice(["rock", "paper", "scissors"])
    UserChoice = input("Choose ROCK, PAPER, OR SCISSORS:")
    print("\nUserChoice:", UserChoice, "\nComputerChoice:", ComputerChoice, "\n")

    if ComputerChoice == UserChoice:
        print("This is a tie.\n")
        # UserChoice = input("Choose ROCK, PAPER, OR SCISSORS: ")

    elif ComputerChoice == "rock":
        if UserChoice == "paper":
            print("You won this round!")
            UserCounter += 1

        else:
            print("You Loose!")
            ComputerCounter += 1

    elif ComputerChoice == "paper":
        if UserChoice == "scissors":
            print("You won this round!")
            UserCounter += 1

        else:
            print("You Loose!")
            ComputerCounter += 1

    elif ComputerChoice == "scissors":
        if UserChoice == "rock":
            print(""You won this round!"")
            UserCounter += 1

        else:
            print("You Loose!")
            ComputerCounter += 1

    # x += 1
print(ComputerCounter, UserCounter)

if UserCounter >= 2:
    print("You Won the Game! :)","\U0001f600")

elif ComputerCounter >= 2:
    print("You lost the game.", "\U0001F612")

# elif ComputerCounter == UserCounter:
#     print("This game is a tie")


    # rounds += 1
    # if rounds == 3:
        # break

# if the computer wins add 1 point to the computer, but if the user wins add 1 point to the user
