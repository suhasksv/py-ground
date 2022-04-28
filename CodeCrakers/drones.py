x = 0
drone_chk = [112, 334, 4444, 4444, 445, 112, 27466, 445, 27466]
for i in drone_chk:
	x ^= i
print("The missing drone order ID is:", x)
