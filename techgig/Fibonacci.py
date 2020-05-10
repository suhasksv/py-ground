def main():
    n = int(input(""))

    prev = 0
    curr = 1
    nex = 0
    print ("{} {} ".format(prev, curr), end='')
    for i in range(2, n):
        nex = prev + curr
        prev = curr
        curr = nex
        print(" {}".format(nex), end='')


main()