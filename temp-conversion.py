print("Converting F to C")
fe = float(input("Enter the Temperature in Fahrenheit: "))
cel = (5.0 * fe - 160.0) / 9.0
print(cel)
"""
print("Converting C to F")
ce = float(input("Enter the Temperature:"))
fe =
"""

# finding degrees C to degrees F
def c(x):
    return (x - 32) * 5 / 9


for i in range(0, 101, 5):
    print("{:>3} F = {:>6.2f} C".format(i, c(i)))
    # format first specifics align it to 3 spaces and in the second specifics align it to 6 spaces and print exactly
    # 2 decimal places
print("\n")
