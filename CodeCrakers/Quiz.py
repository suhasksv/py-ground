import time


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry wrong answer.Try again:")
            attempt = attempt + 1
    if attempt == 3:
        print("The correct answer is " + answer)


score = 0
print("Welcome to the world out of Corona, 2021", "  -  ", "Just for fun")
print("Guess the correct answer you have 3 attempts! Happy Quiz")

guess1 = input("Which is the first private company which launched the Astronauts in to space? :")
check_guess(guess1, "SpaceX")
guess2 = input("What is the name of the capsule used for sending Astronauts? :")
check_guess(guess2, "Dragon")
guess3 = input("Which is the latest Gaming Console realised by Google? :")
check_guess(guess3, "Stadia")
guess4 = input("Did Microsoft make Hologram?(Enter Yes/No) :")
check_guess(guess4, "Yes")
guess5 = input("Which famous cricketer, born on July 8, led India to two consecutive Champions Trophy/ ICC Knockout "
               "finals? :")
check_guess(guess5, "Saurav Ganguly")
guess6 = input("which ia case sensitive programing language?\n \
A)QBASIC\n B)CMD\n C)PYTHON\n D)HTML5\n \
Type A,B,C,D ")
check_guess(guess6, "C")
guess7 = input("Malala Yousafzai, the youngest person ever to win the Nobel Peace Prize, recently completed her "
               "degree from which university in UK? :")
check_guess(guess7, "University of Oxford")

print("Thank You for your patience, your Record have been recorded and soon you will get the score!")
print("Your score is being processed!!")
time.sleep(2)
print("Your score is " + str(score))
