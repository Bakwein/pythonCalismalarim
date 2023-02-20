print("Faktoryel bulma programı!\n Çıkış için -> q")

while True:
    a = input("Faktoryel hesaplamak için hesaplamak istediğiniz sayiyi cikis için q giriniz: ")
    if(a == "q"):
        print("Cikis yapildi!")
        break
    else:
        cevap = 1
        b = int(a)
        for a in range(2,b+1):
            cevap *= a
    print(cevap)



