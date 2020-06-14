word = input("Enter the word to check is it a palendrom or not:")
y = x = i = 0
x = len(word)
y = word[x-1]
i = word[0]

for i in word:
	if i == y:
		y = y - 1
		i = i + 1
if i == y:
        print(word, "is a palendrom")
else:
        print(word, "is not a palendrom")
