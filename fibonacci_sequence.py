prev = 0
curr = 1
nex = 0

try:
    n = int(input("Enter how many fibonacci number to be printed:"))
    for i in range(n):
        print(nex, end=" ")
        prev = curr
        curr = nex
        nex = prev + curr
except:
    print("Invalid Input, enter an integer")
    exit(1)
