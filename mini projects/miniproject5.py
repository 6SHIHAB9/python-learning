print("""Welcome to Treasure Island.
Your mission is to find the treasure.""")

first_choice = input("Where do you want to go? Left or Right?\n")

if first_choice.lower() == "left":
    second_choice = input("Do you want to swim or wait?\n")
    if second_choice.lower() == "wait":
        third_choice = input("Which door do you want to choose? Red,Yellow and Blue\n")
        if third_choice.lower() == "yellow":
            print("You win!!!!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")