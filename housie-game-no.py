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
        if len(no) == 99:
            print("Game over")
            break

        """
        if ans == "print drawn":
            for i in no:
                print(i)
       """
