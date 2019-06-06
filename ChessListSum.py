a = [0 for j in range(64)]
sqr = 1
for i in range(0, 64):
    a[i] = sqr
    sqr = sqr +sqr
    print(i ,a[i])

total = 0
for k in range(0, 64):
    total = total + a[k]
print("Total is:", total)

