def main():
	num = 1
	try:
		row = int(input("Enter an integer:"))
	except:
		print("Invalid Input")
		main()

	for i in range(row, 0, -1):
		for j in range(i, 0, -1):
			print("{:>3}".format(num), end=" ")
			num += 1
		print("")

main()
