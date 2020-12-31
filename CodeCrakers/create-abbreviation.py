# finding short forms of a string
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()


# print(initials("Universal Serial Bus"))  # Should be: USB
# print(initials("local area network"))  # Should be: LAN
# print(initials("Operating system"))  # Should be: OS
w = 1
while w == 1:
    ask = input("Enter a string to convert it to short form :")
    print(initials(ask))

    ask_new = input("Type 'y' to convert another string :").lower()
    if ask_new != "y":
        w += 1
