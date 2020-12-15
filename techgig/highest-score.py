# Created a main function
def main():
    score = []	# Initialized an array with variable name score
    num = int(input(""))	# accepted a input
    for i in range(num):	# initiallzed a for loop for muliple inputs; ends after 'num' iterations
        sc = int(input(""))
        score.append(sc)
    print(max(score))


main()
