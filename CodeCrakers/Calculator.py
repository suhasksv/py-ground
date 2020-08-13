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
time.sleep(3.0)
print("This is a Python Calculator")
time.sleep(2.0)
print("Let's start calculating")
time.sleep(2.0)
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


while True:
    op = input("Enter operation")
    num2 = int(input("Enter an integer"))


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


    tar = calculation()
    print(num1, op, num2, " = ", tar)
    num1 = tar


"""

# main python proghram
response = ['Welcome to smart calculator', 'My name is TeamAlphaCoders Calculator',
            'Thanks for enjoy with me ', 'Sorry ,this is beyond my ability']


# fetching tokens from the text command
def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

    # calculating LCM


def lcm(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


# calculating HCF
def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


# Addition
def add(a, b):
    return a + b

    # Subtraction


def sub(a, b):
    return a - b

    # Multiplication


def mul(a, b):
    return a * b

    # Division


def div(a, b):
    return a / b

    # Remainder


def mod(a, b):
    return a % b

    # Response to command


# printing - "Thanks for enjoy with me" on exit
def end():
    print(response[2])
    input('press enter key to exit')
    exit()


def myname():
    print(response[1])


def sorry():
    print(response[3])

    # Operations - performed on the basis of text tokens


operations = {'ADD': add, 'PLUS': add, 'SUM': add, 'ADDITION': add,
              'SUB': sub, 'SUBTRACT': sub, 'MINUS': sub,
              'DIFFERENCE': sub, 'LCM': lcm, 'HCF': hcf,
              'PRODUCT': mul, 'MULTIPLY': mul, 'MULTIPLICATION': mul,
              'DIVISION': div, 'MOD': mod, 'REMANDER'
              : mod, 'MODULAS': mod}

# commands
commands = {'NAME': myname, 'EXIT': end, 'END': end, 'CLOSE': end}

print('--------------' + response[0] + '------------')
print('--------------' + response[1] + '--------------------')

while True:
    print()
    text = input('enter your queries: ')
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                print(r)
            except:
                print('something went wrong going plz enter again !!')
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
"""