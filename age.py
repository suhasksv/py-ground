try:
    age = int(input("Enter your age:"))
    if age >= 17:
        print("you are an Adult ")
    else:
        print("you aren't an Adult")
except:
    print("Enter an integer")
    exit(1)

# finding the maximum value. Use max() function
max(22, 55, 666, 211125436, 88451485, 3, 5, 5455, 846, 55, 5645, 55, 4, 5555441854)

# finding the minimum value. Use min() function
min(2222524542656, 65252, 552, 522, 245522521452, 2525212, 4321, 5, 2, 0)

# to convert text to uppercase, use .upper() function
print("bang the door!!".upper())

# for replacing a string or an integer use replace() function
m = "time dood"
print(m.replace("dood", "pass"))

# for reversing a string use .reverse() function
# f = "this is a ball"
# f.reverse()

# for loops
for i in range(10):
    for j in range(i, 10):
        print("[" + str(i) + "|" + str(j) + "]", end="\t")
    print("")
print("\n")
