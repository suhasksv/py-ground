import numpy as np
import array as arr


def summ(i):
    return 10 + int(i)


def directCalc():
    subjects = 5
    sums = [0, 0, 0, 0, 0]

    n = int(input("enter number students:"))

    for i in range(0, n):
        s = input("name of student physics chemistry maths english telugu:").split(' ')
        s = s[1:]
        for j in range(0, subjects):
            sums[j] += int(s[j])

    for j in range(0, subjects):
        print(format(sums[j] / n, '.2f'), end=" ")

def main():
    n = int(input("enter number students:"))

    a = []

    subs = 5

    for i in range(1, n + 1):
        s = input("name of student physics chemistry maths english telugu:").split(' ')
        s = s[1:]
        a.append(list(map(int, s)))

    # a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15] [16,17,18,19,20], [21,22,23,24,25] , [26,27,28,29,30]]
    ab = np.array(a).transpose()

    avg = []

    for i in range(0, subs):
        su = 0
        for j in range(0, n):
            print(ab[i, j])
            su += ab[i, j]
        avg.append(su / n)

    print("sums of marks")
    for i in range(0, len(avg)):
        print(format(avg[i], '.2f'))


# def main1():
#     n = int(input("enter number students:"))
#
#     a = []
#
#     subs = 5
#
#     for i in range(1, n + 1):
#         s = input("name of student physics chemistry maths english telugu:").split(' ')
#         s = s[1:]
#         a.append(list(map(int, s)))
#
#     a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25], [26,27,28,29,30]]
#     ab = np.array(a)
#
#     dim = 0
#
#     if (n>=subs):
#         dim = n
#     else:
#         dim=subs
#
#     avg=[]
#
#     for i in range(0, dim):
#         su = 0
#         for j in range(0, dim):
#             if (n < subs and j < n):
#                 print(ab[j,i])
#                 su += ab[j,i]
#             elif (n >= subs):
#                 print(ab[j,i])
#                 su += ab[j,i]
#         avg.append(su)
#
#     print("sums of marks")
#     for i in range(0,len(avg)):
#         print(avg[i])


# for i in range(0, n):
#     print(a[i])

# for i in range(0, n):

# n=int(input())
# a=input()
# b=input()
# a=a.split(' ')
# b=b.split(' ')
# a=a[1:]
# a=list(map(int,a))
# b=b[1:]
# b=list(map(int,b))
# c=[]
# for i in range(len(a)):
#     d=(a[i]+b[i])/2
#     d=format(d,'.2f')
#     c.append(d)
#     print(c,end='')


directCalc()

# main()
