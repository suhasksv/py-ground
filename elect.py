b=c=d=e=f=g=h=0
while True:
    a = input ("enter a party(cycle,fan,car,glass,hand,lotus else nota):")
    n = int(input("number of votes:"))
    if a == "cycle":
      b += n
    elif a == "fan":
        c = c+n
    elif a == "car":
        d = d+n
    elif a == "glass":
        e = e+n
    elif a == "hand":
        f = f+n
    elif a == "lotus":
        g = g+n
    else:
        h = h+n
    i = input("do you want to exit? (y/n)")
    if i == "y":
        break

print ("cycle =",b," has ", (lambda: "lost", lambda: "won")[b>=c]())
print ("fan =",c)
print ("car =",d)
print ("glass =",e)
print ("hand =",f)
print ("lotus =",g)
print ("nota=",h)





    
