y = x = s = a = 0
while True:
	itemprice = int(input("Enter the Price of the item:"))
	quantity = int(input("Enter the Quantity:"))
	y = itemprice
	x = quantity
	s = s + (y * x)
	print("Itemprice", "quantity", "sum")
	print("  ", y,"     ", x, "   ", s)
	i = input("do you want to exit? (y/n)")
        if i == "y":
            breakpoint
