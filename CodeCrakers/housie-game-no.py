import random
import os

no = []
input("Do you want to Draw number?")


def find(numb):
    while True:
        ask = int(input("Enter the number that you want to find:"))
        if ask in numb:
            print("{} has been drawn".format(ask))
        else:
            print("{} is not yet drawn\nPlease wait patiently".format(ask))

        ques = input("Do you want to find another number? Type 'y' to find...... : ").lower()
        if ques == "y":
            continue
        break


while True:
    cho = random.randrange(1, 100)
    if cho not in no:
        no.append(cho)
        print("Picked #:", cho)
        # ans = input("Do you want to print next number?")
        no.sort()
        print("Drawn Numbers:", no)
        ans = input("Do you want to print next number?").lower()
        if ans == "clear":
            os.system('clear')
        elif ans == "find":
            find(no)
        
        if len(no) == 99:
            print("Game over")
            break

        """
        if ans == "print drawn":
            for i in no:
                print(i)
       """
