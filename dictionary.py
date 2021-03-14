lang = {"Python": 1, "Java": 2, "Go": 3, "Kotlin": 4}
print(lang)

for i in lang:
    print(i)

print(lang["Kotlin"])

del lang["Java"]
print(lang)

lang["Go"] = 2
lang["Kotlin"] = 3

print(lang)

for i in lang:
    print(i)

fruits = {"Apples": 20, "Bananas": 40, "Mangoes": 50, "cherries": 100}
print(fruits)

for i in fruits:
    print(i)

del fruits["cherries"]
print(fruits)

for i in fruits:
    print(i)

fruits["Apples"] = 30
fruits["Watermelon"] = 2
print(fruits)

for i in fruits:
    print(i)
print("    ")
if "Watermelon" in fruits:
    print("It is There")

qw = {"apple", "banana", "cherries", }