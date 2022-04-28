num = [20, 40, 10, 80, 6, 7]
f = 0
j = 0
a = 0
for i in range(100):
	if num[j] > num[j+a]:
		print(f, end=" ")
		j += 1
		f = 0
		a = j + 2
	else:
		f += 1
		a += 1
