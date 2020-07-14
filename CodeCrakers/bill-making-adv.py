y = x = s = a = 0
while True:
    item_price = int(input("Enter the Price of the item:"))
    quantity = int(input("Enter the Quantity:"))
    y = item_price
    x = quantity
    s = s + (y * x)
    print("Item_price", "quantity", "sum")
    print("  ", y, "     ", x, "   ", s)
    i = input("do you want to exit? (y/n)")
    if i == "y":
        break
