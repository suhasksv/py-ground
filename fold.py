while True:
    a = int(input("Enter number of folders:"))
    if a > 0 and a < 10:
        i=a
        while i>0:
            b = int(input("Enter number of files:"))
            c = input("Enter names of files:")
            d = c.split()
            if b != len(d):
                print("input error!!")
            print(d)
            i = i-1    
    else:
        print ("input error!!")
    e = input("do you want to creat more folders and files?(y/n) ")
    if e == "n":
        break
