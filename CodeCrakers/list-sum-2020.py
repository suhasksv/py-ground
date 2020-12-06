num = [1020, 1201, 1209, 2002, 18, 2000, 20]
se = []

text_file = open("list-sum-2020.txt", "r")
content = text_file.readlines()
content = [x.strip() for x in content]
print (content)

content = [int(i) for i in content]

for i in content:
    for j in content:
        if i not in se and j not in se:
            if i + j == 2020:
                print(i, "+", j, " = 2020")
                se.append(j)
                se.append(i)
        continue

