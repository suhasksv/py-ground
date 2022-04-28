# defining a function
def greet(friends):
    for i in friends:
        print("Hi", i)


friend = ["Python", "Go", "HTML5", "Java", "C", "C++"]
greet(friend)
print("\n")

def price(price):
    tax = (price * 0.06)
    final = tax + price
    return "The price without tax is ${:.2f}, tax is ${:.2f} and final price with tax is {:.2f}".format(price, tax, final)

x = 1
while x == 1:
	try:
		prices = float(input("Enter the price of the item :"))
		print(price(prices))
	except:
		print("Please enter an integer or decimal value")
		continue

	ask = input("Do you want to find total price and tax? Enter 'y' to continue...! :").lower()
	if ask != 'y':
		x += 1
