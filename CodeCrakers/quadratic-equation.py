import cmath
import time

print("Welcome to Quadratic Equation Solver")
time.sleep(1)
print("Input Format - ax**2 + bx + c = 0")
time.sleep(1)

q = 0
g = 0

a = (input("Enter the value of 'a':"))
b = (input("Enter the value of 'b':"))
c = (input("Enter the value of 'c':"))

if a.isnumeric():
    q += 2
else:
    print("Invalid input of a {0}".format(a))

# if b.isnumeric():
#     q += 1
# else:
#     print("Invalid input of a {0}".format(b))

if c.isnumeric():
    q += 1
else:
    print("Invalid input of a {0}".format(c))

while q == 3 and g == 0:
    a = int(a)
    b = int(b)
    c = int(c)
    d = (b ** 2) - (4 * a * c)

    alpha = (-b - cmath.sqrt(d)) / (2 * a)
    beta = (-b + cmath.sqrt(d)) / (2 * a)

    z = "The answer of the quadratic equation {0}x**2 + {1}x + {2} ="
    print(z.format(a, b, c), alpha, "or", beta)
    g += 1
