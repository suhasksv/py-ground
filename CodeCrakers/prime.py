def isPrime(n):
    cnt = 0
    for a in range(2, int(n / 2) + 1):
        z = n % a
        if z == 0:
            return False
    return True


m = int(input("Enter an integer:"))
n = int(input("Enter an integer:"))
for i in range(m, n + 1):
    if isPrime(i):
        print(i)
