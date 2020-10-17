try:
    n = int(input("Enter an integer to find the common multiples of 3 and 5:"))
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "fuzz buzz")
        else:
            if i % 3 == 0:
                print(i, "fuzz")
            elif i % 5 == 0:
                print(i, "buzz")
            else:
                print(i)
except:
    print("bash: Input Error! Enter an integer")
    exit(1)
