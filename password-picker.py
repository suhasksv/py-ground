import random
import string

adj = ("sleepy", "beautiful", "white", "purple", "blue", "green", "brave",)
noun = ("apple", "sony", "mediaTek", "snapdragon", "beetal", "bee", "sg", "ss")

print("Welcome to password picker")
while True:
    for num in range(1):
        adjs = random.choice(adj)
        nouns = random.choice(noun)
        num = random.randrange(0, 100)
        spe_char = random.choice(string.punctuation)

        password = adjs + nouns + str(num) + spe_char
        print("Your new password is: %s" % password)

    a = input("Do you want to create another password?(y/n):")
    if a == "n":
        break
