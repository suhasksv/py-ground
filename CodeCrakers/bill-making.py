n = int(input("Enter no. of items:"))
s = 0
for i in range(0, n):
	cost = int(input("Enter the Price of the item"))
	s = s + cost 
Quantity = n
Price = s
Order = "I need to pay ${1} for {0} items "
print(Order.format(Quantity, Price))

