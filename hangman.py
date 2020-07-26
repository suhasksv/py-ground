import random

print("                _ _ _ _           _ _ _   _ _ _            _ _ _ _")
print("\            / |        |        |		 |     | |\    /| |       ")
print(" \          /  |        |        |		 |	   | | \  / | |       ")
print("  \        /   |- -     |        |		 |	   | |  \/  | |- - -  ")
print("   \  /\  /    |        |        | 		 |	   | |	    | |       ")
print("    \/  \/     |_ _ _ _ |_ _ _ _ |_ _ _  |_ _ _| |	    | |_ _ _ _")

while True:
    print("Welcome to Hangman")
    words = ["pizza", "admit", "about", "actor", "acute", "allow", "alert", "along", "black"]
    secret_word = random.choice(words)
    words.remove(secret_word)
    clue = list("_____")
    hs = u"\u2764"
    gwc = False


    def update(guessed_letter, secret_word, clue):
        index = 0
        while index < len(secret_word):
            if guessed_letter == secret_word[index]:
                clue[index] = guessed_letter
            index = index + 1


    difficulty = input("Enter the difficulty level for hangman game \n 1.Easy \n 2.Normal \n 3.Hard \n")
    if difficulty == "1":
        lives = 12
    elif difficulty == "2":
        lives = 9
    else:
        lives = 5

    while lives > 0:
        print(clue)
        print("Lives left:", hs * lives, "   ", lives)
        guess = input("Guess the letter or the whole word: ").lower()

        if guess == secret_word:
            gwc = True
            break

        if guess in secret_word:
            update(guess, secret_word, clue)
        else:
            print("Incorrect answer, you lose a life")
            lives -= 1

    if gwc:
        print("You won by saving:", lives, "live(s)! 🥳")
    else:
        print("Game Over You lost...😭")

    k = input("Do you want to play another game? Type 'y' to continue:")
    if k != "y":
        break
