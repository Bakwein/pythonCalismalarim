ilk = int(input("ilk sayiyi giriniz:"))
diger = int(input("ikinci sayiyi giriniz:"))

a = int(input("Lutfen yapmak istediginiz islemi seciniz(1->Toplama,2->Cikarma,3->Carpma,4->Bolme,5->Mod:)"))
sonuc = None

if (a == 1):
    sonuc = ilk + diger
    print(sonuc)
elif a == 2:
    sonuc = ilk - diger
    print(sonuc)
elif a == 3:
    sonuc = ilk * diger
    print(sonuc)
elif a == 4:
    sonuc = ilk / diger
    print(sonuc)
elif a == 5:
    sonuc = ilk % diger
    print(sonuc)
else:
    print("islemi secerken yanlis sayi girdiniz")