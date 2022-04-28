def chk_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(True)
    else:
        print(False)


try:
    chk = int(input("Enter a year to check if it is a leap year: "))
    chk_year(chk)
except:
    print("Invalid Input, Enter an integer")
    exit(1)
