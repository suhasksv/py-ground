num = 1
try:
    row = int(input("Enter number of rows:"))
except:
    print("Please enter integer")
    exit(1)
for i in range(1, row+1):
    for j in range(0, i):
        print(num, end=" ")
        num += 1
    print("")
