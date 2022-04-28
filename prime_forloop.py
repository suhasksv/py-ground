n = int(input("Enter an integer"))

for i in range (2, int(n/2)):
    reminder = n % i

    print(i)

    if (reminder == 0):
        print(n, " is not a prime number")
        break
else:
    print(n, " is a prime number")

