def main():
	num = 1
	try:
		row = int(input("Enter number of rows:"))
	except:
		print("Invalid Input. Enter an integer")
		exit(1)
	
	for i in range(0, row):
		for j in range(-1, i):
			print(num, end=" ")
			num += 1
		print("")
		if num != 1:
			num = 1


main()
