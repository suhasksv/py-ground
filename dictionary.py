plang = {"Python": 1, "Java": 2, "Go": 3, "Kotlin": 4}
print(plang)

for i in plang:
    print(i)

print(plang["Kotlin"])

del plang["Java"]
print(plang)

plang["Go"] = 2
plang["Kotlin"] = 3

print(plang)

for i in plang:
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
