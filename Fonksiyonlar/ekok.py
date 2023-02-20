
def ekokBulan(a,b):
    x = 2
    ekok = 1
    while True:
        if(a % x == 0 and b % x == 0):
            ekok *= x
            a //= x
            b //= x
        elif(a % x == 0 and b % x != 0):
            ekok *= x
            a //= x
        elif(a % x != 0 and b % x == 0):
            ekok *= x
            b //= x
        else:
            x += 1
        if(a == 1 and b == 1):
            break
    return ekok






while True:
    s1 = input("Sayi1(Cikis icin q):")
    if(s1 == "q"):
        break
    else:
        s1 = int(s1)
    s2 = int(input("Sayi2(Cikis icin q):"))
    if (s2 == "q"):
        break
    else:
        s2= int(s2)
    print(ekokBulan(s1, s2))