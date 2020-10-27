def facto(n):
	if n <= 1:
		return 1
	else:
		return n * facto(n-1)

try:
	n = int(input("Enter an integer:"))
except:
	print("Invalid input")
	exit(1)
print(facto(n))
