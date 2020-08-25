"""num = int(input("How many numbers would like to oparate? "))
s = a = f = ask = 0
for i in range(0, num-1):
    if i == 0:
        a = int(input("Enter the number:"))
    ask = input("Which operation would you like to do?(+, -, *, /, **)")
    f = int(input("Enter the number:"))
    if i == 0:
        if ask == "+":
            s = a + f
        if ask == "-":
            s = a - f
        if ask == "*":
            s = a * f
        if ask == "/":
            s = a / f
        if ask == "**":
            s = a ** f
    if ask == "+":
        s = s + f
    if ask == "-":
        s = s - f
    if ask == "*":
        s = s * f
    if ask == "/":
        s = s / f
    if ask == "**":
        s = s ** f        
print(s)
"""

import time

print("Hi, Welcome to Quantum Tricks")
time.sleep(2.0)

print("This is a Infinity Python Calculator")
time.sleep(1.0)

print("Let's start calculating")
time.sleep(1.0)

num1 = int(input("Enter an integer:"))


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def power(a, b):
    return a ** b


ops = {"+": add, "add": add, "addition": add, "sum": add, "-": sub, "sub": sub, "subtraction": sub, "difference": sub, "x": mul,
       "multiply": mul, "*": mul, "multiplication": mul, "div": div, "division": div, "/": div, "power": power, "^": power, "**": power}


"""
def calculation():
    if op == "+" or "add" or "addition" or "sum":
        return add(num1, num2)

    elif op == "-" or "subtract":
        return sub(num1, num2)

    elif op == "x" or "multiply" or "*":
        return mul(num1, num2)

    elif op == "divide" or "/":
        return div(num1, num2)

    else:
        return power(num1, num2)

"""
while True:
    op = input("Enter operation:")

    if op.lower() in ops:
        num2 = int(input("Enter an integer:"))

        q = eval("ops[op](num1, num2)")
        print(q)
        num1 = q
    else:
        print("Sorry Operation does not exist. Please try another operation.")
        break

    # tar = calculation()
    # print(num1, ops, num2, " = ", )
    # num1 = tar
