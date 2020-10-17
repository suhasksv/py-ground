"""
def main():
    s = input("")
    separator = ","
    print(separator.join(s), end="")


main()
"""


def main():
    s = input("")
    separator = input("")
    x = 0
    while x < 4:
        print('s2.join(s1):', separator.join(s))
        x = x + 1


main()
