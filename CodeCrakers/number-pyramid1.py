def main():
    global row
    try:
        row = int(input("Enter number of rows:"))
        main_func(row)
    except:
        print("Please enter integer")
        exit(1)


def main_func(row):
    num = 1
    for i in range(1, row+1):
        for j in range(0, i):
            print("{:>3}".format(num), end=" ")
            num += 1
        print("")


main()
