num = 1

def factorial(curr):
	g = 1
	for i in range(1, curr+1):
		g *= i
	return g

try:
	row = int(input("Enter number of rows:"))
except:
	print("Invalid input. Please enter an integer")
	exit(1)

for i in range(1, row+1):
	for j in range(0, i):
		print(factorial(num), end = " ")
		num += 1
	print("")
