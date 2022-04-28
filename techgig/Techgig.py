"""
def main():
    a = int(input("Enter an integer"))
    b = int(input("Enter an integer"))
    for i in range(a, b+1):
        c = 0
        for f in range(1, int(i/2)):
            if (i/f) == 0:
                c = c + 1
            if c == 1:
                print(i)
main()
"""


"""
n = int(input("enter an integer:"))

prev = 0
curr = 1
nex = 0

c = 3
#print("{} {}".format(prev, curr), end="")
print(prev, end="")
print("", curr, end="")
while c <= n:
    nex = prev + curr
    prev = curr
    curr = nex
 #   print(" {}".format(nex), end="")
    c += 1
    print ("" ,nex, end="")
"""



