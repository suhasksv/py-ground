def sq(n):
    return int(n) ** 2


def length(s):
    return s + str(len(s))


def string_len():
    s = input("Enter strings to calculate the length:").split()
    f = []
    for i in range(0, len(s)):
        q = len(s[i])
        f.append(s[i] + str(q))
    print(f)


def main():
    num = input("Enter an integer:").split(' ')
    # p = list(map(sq, num))
    # p = list(map(length, num))

    # p = []
    #
    # for i in range(0, len(num)):
    #     s = int(num[i]) ** 2
    #     p.append(s)

    # print(p)


# main()
string_len()

a = input().split()
for i in range(0, len(a)):
    print(a[i])

"""
def array(array1, array2):
    for g, j in zip(array1, array2):
        print(g + j, end="\n")
"""

array1 = [[1, 2], [11, 12]]
array2 = [[3, 4], [13, 14]]

for f in range(0, len(array1)):
    for g, j in zip(array1[f], array2[f]):
        print(int(g + j))

in1 = input("")
in2 = input("")
in3 = input("")
in4 = input("")

in5 = input("")
in6 = input("")
in7 = input("")
in8 = input("")
w = []
b = []
c = []
d = []

x = []
r = []
t = []
u = []

w.append(in1)
b.append(in2)
c.append(in3)
d.append(in4)

x.append(in5)
r.append(in6)
t.append(in7)
u.append(in8)

v = [w, b], [c, d]
k = [x, r], [t, u]
print(v)
print(k)

o = len(max(in1, in2, in3, in4, in5, in6, in7, in8))

for z in range(0, len(in2)):
    for y, s in zip(v[z], k[z]):
        print(int(y + s))
