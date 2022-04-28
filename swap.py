def three_variabe():
    temp = 0
    a = int(input("enter an integer a:"))
    b = int(input("enter an integer b:"))
    temp = a
    a = b
    b = temp
    print("a =", a)
    print("b =", b)

def add_swap():
    a = int(input("enter an integer a:"))
    b = int(input("enter an integer b:"))
    a = a + b
    b = a - b
    a = a - b
    print("integer a is:", a)
    print("integer b is:", b)

def mul_swap():
    a = float(input("enter an integer a:"))
    b = float(input("enter an integer b:"))
    a = float(a * b)
    b = float(a / b)
    a = float(a / b)
    print("integer a is:", a)
    print("integer b is:", b)
total = mul_swap(),add_swap(),three_variabe()
print(total)
