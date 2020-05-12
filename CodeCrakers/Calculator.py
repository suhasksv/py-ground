num = int(input("How many numbers would like to oparate? "))
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
