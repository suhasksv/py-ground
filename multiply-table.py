# declaring a user defined function
def multiply(start, stop):
    for i in range(start, stop + 1):
        for j in range(1, stop + 1):
            x = i * j
            print(str("{:.2f}").format(x), end=" ")
        print()


multiply(1, 10)
