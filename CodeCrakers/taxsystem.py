# noinspection PyInterpreter

salary = int(input("Enter your salary:"))
a = b = c = d = e = 0
tax1 = tax2 = tax3 = tax4 = tax5 = 0
total_tax = amt = 0
if 250000 <= salary <= 500000:
    a = salary - 250000
    tax1 = a * 0.5
    amt += a - tax1

if 500000 <= salary <= 750000:
    b = salary - 2250000
    tax2 = b * 0.10
    amt += b - tax2

if 750000 <= salary <= 1000000:
    c = salary - 250000
    tax3 = b * 0.15
    amt += c - tax3

if 1000000 <= salary <= 1500000:
    d = salary - 250000
    tax4 = d * 0.20
    amt += d - tax4

if salary >= 2000000:
    e = salary
    tax5 = e * 0.30
    amt += e - tax5

total_tax = tax1 + tax2 + tax3 + tax4 + tax5
print("Your Salary is:", salary)
print("Tax that you should pay:", total_tax)
print("You get:", amt)
