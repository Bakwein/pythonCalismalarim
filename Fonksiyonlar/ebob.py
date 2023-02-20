def ebobBulan(a,b):
    enBuyuk = 0
    enKucuk = 0
    cevap = 0
    if(a >= b):
        enBuyuk = a
        enKucuk = b
    else:
        enBuyuk = b
        enKucuk = a
    for s in range(1,enKucuk+1):
        if(enKucuk % s == 0 and enBuyuk % s == 0):
            cevap = s
    return cevap



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
    print(ebobBulan(s1, s2))