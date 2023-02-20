def tekCift(a):
    if(a % 2 == 0):
        return a
    else:
        raise ValueError("Tek sayi girdiniz")


liste = [23,2,61,4,1,13,22,51]
for eleman in liste:
    try:
        print(tekCift(eleman))
    except ValueError:
        pass
