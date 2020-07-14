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


num1 = int(input("Enter the first number:"))
op1 = input("Enter the first operation:")
num2 = int(input("Enter the second number:"))


def ope():
    if "+" or "add" or "addition" or "sum":
        return add(num1, num2)


def ope2():
    if "-" or "subtract":
        return sub(num1, num2)


def ope3():
    if "x" or "multiply" or "*":
        return mul(num1, num2)


def ope4():
    if "divide" or "/":
        return div(num1, num2)


def ope5():
    if "power" or "**" or "^":
        return power(num1, num2)
