from art import logo
import random


def game():
    def onboarding():
        print(logo)
        print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
        guess = random.randint(1,100)
        return guess

    guess = onboarding()

    def choose_difficulty():
        difficulty= input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty.lower() == "easy":
            no_of_guesses = 10
        else:
            no_of_guesses = 5
        return  no_of_guesses

    no_of_guesses = choose_difficulty()



#make the user guess
    while True and no_of_guesses > 0:
        print(f"You have {no_of_guesses} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == guess:
            print(f"You got it! The answer was {guess}")
            break
        elif user_guess < guess:
            print("Too low.\nGuess again.")
        else:
            print("Too high.\nGuess again")
        no_of_guesses -= 1

    else:
        print("You've run out of guesses, you lose.")
game()