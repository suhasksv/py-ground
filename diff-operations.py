import time

print("Hi, Welcome to Quantum Tricks")
time.sleep(1.0)
print("This a different operations calculator using same numbers")
time.sleep(2.0)
print("Lets start calculating")
time.sleep(1.0)

num1 = int(input("Enter an integer:"))
num2 = int(input("Enter an integer:"))


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


ops = {"+": add, "add": add, "addition": add, "sum": add, "-": sub, "sub": sub, "subtraction": sub, "difference": sub, "x": mul,
       "multiply": mul, "*": mul, "multiplication": mul, "div": div, "division": div, "/": div, "power": power, "^": power,
       "**": power, "mod": mod, "%": mod, "||": mod, "| |": mod, }

while True:
    op = input("Enter an operation:")
    if op.lower() in ops:
        print(eval("ops[op](num1, num2)"))
    else:
        print("Sorry operation does not exists. Please try again")
