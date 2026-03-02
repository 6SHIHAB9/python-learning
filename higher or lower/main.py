import art
from game_data import data
import random

def ui(score,A,B):
    if score != 0:
        print(f"You're right! Current score {score}")

    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]} ")

    print(art.vs)
    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]} ")

def biggest(A,B):
    if A["follower_count"] > B["follower_count"]:
        return A
    else:
        return B


A = random.choice(data)
score = 0

while True:
    print(art.logo)
    B = random.choice(data)

    ui(score,A,B)

    choice = input("Who has more followers? Type 'A' or 'B': ")

    big = biggest(A,B)

    if choice.lower() == "a":
        cho = A
    elif choice.lower() == "b":
        cho = B

    if cho == big:
        score += 1
        print("\n" * 100)
        A = big
    else:
        print("\n" * 100)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break


