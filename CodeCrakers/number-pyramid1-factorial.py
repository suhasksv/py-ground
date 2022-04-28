def factorial(curr):
    g = 1
    for i in range(1, curr + 1):
        g *= i
    return g


def non_recurrsion():
    num = 1
    try:
        row = int(input("Enter number of rows:"))
    except:
        print("Invalid input. Please enter an integer")
        exit(1)

    for i in range(1, row + 1):
        for j in range(0, i):
            print(factorial(num), end=" ")
            num += 1
        print("")


# Recursive statement included
def factorial_recursion(numb):
    if numb == 1:
        return 1
    else:
        return numb * factorial_recursion(numb - 1)


def recursion():
    num = 1
    try:
        row = int(input("Enter number of rows:"))
    except:
        print("Invalid input. Please enter an integer")
        exit(1)

    for i in range(1, row + 1):
        for j in range(0, i):
            print(factorial_recursion(num), end=" ")
            num += 1
        print("")


non_recurrsion()

# recursion()
