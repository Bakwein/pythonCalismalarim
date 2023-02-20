def asal_sayi_mi(x):
    flag = 0
    if(x < 2):
        print(x , "bir asal sayi değil")
        return 0
    for a in range(2,x):
        if(x % a == 0):
            flag += 1
    if(flag > 0):
        print(x , "bir asal sayi değil")
        return 0
    print(x , "bir asal sayi")

while True:
    sayi = input("Sayi(Çıkış için -> q):")
    if(sayi == "q"):
        break
    asal_sayi_mi(int(sayi))



