import random
import os

no = []
input("Do you want to Draw number?")
while True:
    cho = random.randrange(1, 100)
    if cho not in no:
        no.append(cho)
        print("Picked #:", cho)
        # ans = input("Do you want to print next number?")
        no.sort()
        print("Drawn Numbers:", no)
        ans = input("Do you want to print next number?")
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
def find(numli):
    ask = int(input("Enter the number that you want to find:"))
    if ask in numli:
        print("{} has been drawn").format(ask)
    else:
        print("{} is not drawn").format(ask)
