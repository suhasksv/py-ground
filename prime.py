n = int(input("Enter an integer:"))
cnt = 0
i = 1

while (i <= n):
    if (n % i == 0):
        cnt = cnt + 1
    i = i +1

if (cnt > 2):
    print (n ," is not a prime number")
else:
    print (n ," is a prime number")
