import random

assets = ["ROCK","PAPER","SCISSORS"]

user = int(input("What do you want to choose? 0 for Rock,1 for Paper,2 for Scissors.\n"))
if user == 0 or user == 1 or user == 2:
    print("You choose:")
    print(assets[user])

    computer = random.randint(0,2)
    print("\nComputer choose:")
    print(assets[computer])

    print()

    if user == 0 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 0:
        print("You Lose")
    elif user == computer:
        print("Its a tie")
    else:
        print("You Won")
else:
    print("Please select a valid option!")


