text_file = open("input.txt", "r")
content = text_file.readlines()

# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list#
content = [x.strip() for x in content]

# https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
content = [int(i) for i in content]
# Problem 1
v1 = 0
prev = content[0]
for g in content:
    if g > prev:
        v1 += 1
    prev = g
print(v1)

# Problem 2 
prev = 0
v2 = 0
f = content[0]

for f in range (0, len(content)-3):
    s = content[f] + content[f+1] + content[f+2]
    
    if s > prev:
        v2 += 1
    prev = s
print(v2)
