def mukemmelMi(x):
    toplam = 0
    for s in range(1,x):
        if(x % s == 0):
            toplam += s
    if(toplam == x):
        return 1
    return 0




for a in range(1,1001):
    if(mukemmelMi(a)) == 1:
        print(a, "bir mukemmel sayi!")
    ###else:
       ### print(a,"bir mukemmel sayi degil!")
