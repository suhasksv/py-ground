import random

words = ("random", "choice", "source", "pizzah", "fpizza", "python")
secret_word = random.choice(words)
clue = list("??????")
hs = u"\u2764"
guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1


diffs = input("Choose difficulty (type 1/2/3):\n 1. easy \n 2. normal \n 3. hard\n")
diff = int(diffs)
if diff == 1:
    lives = 12
elif diff == 2:
    lives = 9
else:
    lives = 5

while lives > 0:
    print(clue)
    print("lives left: " + hs * lives, "  ", lives)
    guess = input("Guess a letter or the whole word: ")

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print("Incorrect, You lose a life")
        lives = lives - 1

    if guessed_word_correctly:
        print("You won! the word was " + secret_word)
    else:
        print("You lost!", "", "Total number of lives left:", lives)
