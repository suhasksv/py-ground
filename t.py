g = 1
c = 1

for i in range(2, 65):
    c = c * 2
    g = g + c
    print(i, c)
print("The sum is: ", g)
