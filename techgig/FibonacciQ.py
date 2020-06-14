def main():
    n = int(input("How many number of fibonacci numbers do you want to generate?"))

    prev = 0
    curr = 1
    next = 0

    counter = 3

    result = " "+str(prev)+ " "+str(curr)

    while counter <= n :
        next = prev + curr
        result = result + " "+ str(next)
        prev = curr
        curr = next
        counter += 1

    print (result)
main()
