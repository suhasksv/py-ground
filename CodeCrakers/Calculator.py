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
