import random
import string

adj = ("sleepy", "beautiful", "white", "purple", "blue", "green", "brave",)
noun = ("apple", "sony", "mediaTek", "snapdragon", "beetle", "bee", "sg", "ss")

print("Welcome to password picker")
while True:
    num: int
    for num in range(1):
        adjectives = random.choice(adj)
        nouns = random.choice(noun)
        num = random.randrange(0, 100)
        spe_char = random.choice(string.punctuation)

        password = adjectives + nouns + str(num) + spe_char
        print("Your new password is: %s" % password)

    a = input("Do you want to create another password? Enter 'Y' to continue....::").lower()
    if a == "n":
        break
