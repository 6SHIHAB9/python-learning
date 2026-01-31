import random

stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]



#Choose a random word from liest
words = ["camel","lion","tiger","zebra","rabbit"]

word_chosen = random.choice(words)
print(word_chosen)

#Show empty place holder
place_holder =""

for i in range(len(word_chosen)):
    place_holder += "_"
print(place_holder)


wrong_guess = 0


while True:
    #Take user guess
    letter = input("Guess a letter: ").lower()

    if letter in place_holder:
        print("You already got it right!!! choose a different letter.")

    #If guess is correct replace placeholders with correct guess
    elif letter in word_chosen:
        list_placeholder = list(place_holder)
        loop = 1
        for i in word_chosen:
            if i == letter:
                list_placeholder[loop-1] = letter
            loop += 1
        
        place_holder = ""
        for i in list_placeholder:
            place_holder += i
    else:
        wrong_guess += 1

    print(place_holder)
    print(stages[wrong_guess])



    if place_holder == word_chosen:
        print("You win")
        break

    elif wrong_guess >= 6:
        print("You lose")
        break


