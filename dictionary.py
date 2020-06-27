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
