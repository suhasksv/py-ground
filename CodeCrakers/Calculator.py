import time

print("Hi, Welcome to Quantum Tricks")
time.sleep(2.0)

print("This is a Infinity Python Calculator")
time.sleep(1.0)

print("Let's start calculating")
time.sleep(1.0)

num1 = int(input("Enter an integer:"))


# Calculating addition
def add(a, b):
    return a + b


# Calculating subtraction
def sub(a, b):
    return a - b


# Calculating multiplication
def mul(a, b):
    return a * b


# Calculating division
def div(a, b):
    return a / b


# Calculating exponent
def power(a, b):
    return a ** b


# Calculating mod
def mod(a, b):
    return a % b


# Defining a Dictionary of Operations
ops = {"+": add, "add": add, "addition": add, "sum": add, "-": sub, "sub": sub, "subtraction": sub, "difference": sub,
       "x": mul,
       "multiply": mul, "*": mul, "multiplication": mul, "div": div, "division": div, "/": div, "power": power,
       "^": power,
       "**": power, "mod": mod, "%": mod, "||": mod, "| |": mod, }
# Main loop of calculation
while True:
    op = input("Enter operation:")              # Takes input from the costumer and stores in variable op

    if op.lower() in ops:
        num2 = int(input("Enter an integer:"))

        q = eval("ops[op](num1, num2)")         # eval is function in python that evaluates the value of the given operation(op)
        print(q)
        num1 = q
    else:
        print("Sorry Operation does not exist. Please try another operation.")
