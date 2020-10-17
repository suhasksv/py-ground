def chk_year(year):
	if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
		print(True)
	else:
		print(False)

chk = int(input("Enter a year to check if it is a leap year: "))

chk_year(chk)
