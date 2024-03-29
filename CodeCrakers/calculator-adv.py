# Calculating xor or exclusive or
def xor(a, b):
    return a ^ b


# Calculating or
def of(a, b):
    return a or b


# Calculating and
def anda(a, b):
    return a and b


# Calculating Bit wise and
def bitand(a, b):
    return a & b


# Calculating Bit wise or
def bitor(a, b):
    return a | b


# Defining a Dictionary of Operations
ops = {"+": add, "add": add, "addition": add, "sum": add, "-": sub, "sub": sub, "subtraction": sub,
       "difference": sub,
       "x": mul,
       "multiply": mul, "*": mul, "multiplication": mul, "div": div, "division": div, "/": div, "power": power,
       "^": power,
       "**": power, "mod": mod, "%": mod, "||": mod, "| |": mod, "xor": xor, "^or": xor, "exclusive_or": xor,
       "or": of,
       "and": anda, "bitand": bitand,
       "&": bitand, "bitor": bitor, "bitwiseor": bitor, "bit-wise-or": bitor}

# Main loop of calculation
while True:
    op = input("Enter operation:")  # Takes input from the costumer and stores in variable op

    if op in ops:
        try:
            num2 = float(input("Enter an integer:"))
            answer = eval("ops[op](num1, num2)")
            # eval is function in python that evaluates the value of the given operation(op)
            print(answer)
            num1 = answer
        except:
            print("Invalid Input. Please try again by entering a number")
    elif op.lower() == "end" or op.lower() == "finish" or op.lower() == "break connection" or op.lower() == "break" or op.lower() == "exit" or op.lower() == "exit":
        print("")
        print("This is your final result:", answer)
        print("Thanks for Choosing Quantum Tricks Infinity Python Calculator")
        break
    else:
        print("Sorry Operation does not exist. Please try another operation.")
        print("")

