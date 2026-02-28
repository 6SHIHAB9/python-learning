import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def score(cards_list):
    scorie = 0
    for i in cards_list:
        scorie += i
    if scorie > 21:
        if 11 in cards_list:
            scorie -= 10
    return scorie

def result(l1_cards,l2_cards,hscore,cscore):
    winner = None
    if hscore == cscore:
        print("Draw 🙃")
    elif hscore <= 21 and cscore > 21:
        print("Opponent went over. You win 😁")
    elif hscore > cscore and hscore <= 21:
        print("You win 😃")
    elif hscore > 21:
        print("You went over. You lose 😭")
    elif hscore < cscore and cscore <= 21:
        print("You lose 😤")



    return winner
while True:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if start == 'y':
        end = False
        print("\n" * 100)
        print(logo)

        h_cards = [random.choice(cards),random.choice(cards)]
        c_cards = [random.choice(cards),random.choice(cards)]

        while True:
            h_score = score(h_cards)
            c_score = score(c_cards)

            print(f"Your cards: {h_cards}, current score: {h_score}")
            print(f"Computer's first card: {c_cards[0]}")

            if h_score > 21:
                end = True

            else:
                flow = input("Type 'y' to get another card, type 'n' to pass: ")

                if flow == "y":
                    h_cards.append(random.choice(cards))
                else:
                    end = True

            if end:
                while c_score <= 16:
                    c_cards.append(random.choice(cards))
                    c_score = score(c_cards)

                print(f"Your final hand: {h_cards}, final score: {h_score}")
                print(f"Computer's final hand: {c_cards}, final score: {c_score}")

                result(h_cards,c_cards,h_score,c_score)
                break
