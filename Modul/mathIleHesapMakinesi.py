import math

while True:
    a = input("Yapmak istediginiz islemi giriniz(1->Toplama 2->Toplama 3->Cikarma 4->Bolme 5->Mod-Çıkış 6->Mutlak Deger Çıkış için ->Q):")
    if(a == "q"):
        print("Cikis yapildi!")
        break
    if(a == "1"):
        s1 = int(input("İlk sayi:"))
        s2 = int(input("İkinci sayi:"))
        print(s1 + s2)
    elif(a == "2"):
        s1 = int(input("İlk sayi:"))
        s2 = int(input("İkinci sayi:"))
        print(s1-s2)
    elif(a == "3"):
        s1 = int(input("İlk sayi:"))
        s2 = int(input("İkinci sayi:"))
        print(s1*s2)
    elif(a == "4"):
        s1 = int(input("İlk sayi:"))
        s2 = int(input("İkinci sayi:"))
        if(s2 == 0):
            print("Bir sayi 0'a bolunemez")
            break
        print(s1 / s2)
    elif(a == "5"):
        s1 = int(input("İlk sayi:"))
        s2 = int(input("İkinci sayi:"))
        print(s1 % s2)
    elif(a == "6"):
        s1 = int(input("Sayiyi giriniz:"))
        print(math.fabs(s1))

