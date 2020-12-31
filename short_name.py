def name_tag(first_name, last_name):
    return "{}" " " "{}.".format(first_name, last_name[0])


# print(name_tag("Jane", "Smith"))  # Should display "Jane S."
# print(name_tag("Francesco", "Rinaldi"))  # Should display "Francesco R."
# print(name_tag("Jean-Luc", "Grand-Pierre"))  # Should display "Jean-Luc G."

x = 1
while x == 1:
	ask = input("Enter Full name of to make it short :")
	name_tag(ask)

	ask_new = input("Do you want to find another one? (y/n)").lower()
	if ask_new == 'y':
		continue
	break

# g = 1
# c = 1

# for i in range(2, 65):
#     c = c * 2
#     g = g + c
#     print(i, c)
# print("The sum is: ", g)
