def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print ("Correct answer")
            score = score + 1
            still_guessing = False
        else:
             if attempt < 2:
                 guess = input("Sorry wrong answer.Try again:")
             attempt = attempt + 1
    if attempt == 3:
            print("The correct answer is "+ answer)
score = 0
print ("Guess the animal you have 3 attempts")
guess1 = input("Which animal lives in polar region? ")
check_guess(guess1, "Polar bear")
guess2 = input ("Which animal is the largest animal? ")
check_guess(guess2, "blue whale")
guess3 = input("Which is the fastest bird on Earth? ")
check_guess(guess3, "Falcon")
guess4 = input("Which is the largest contitent? ")
check_guess(guess4, "asia")
guess5 = input("Which is the leaf which exactly match with a pokemon's name? ")
check_guess(guess5, "Bay leaf")
guess6 = input("whish ia case sensitive programmimng language?\n \
A)QBASIC\n B)DOLPHIN\n C)PYTHON\n D)HTML5\n \
Type A,B,C,D ")
check_guess(guess6, "C")
guess7 = input("Is it 1616 year today? Type true or false ")
check_guess(guess7, "false")
print("Your score is " + str(score))
