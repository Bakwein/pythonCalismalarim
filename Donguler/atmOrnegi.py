print("Atm'ye hosgeldiniz!\n1->Para Yatirma\n2->Para Çekme\n3->Bakiye Sorgulama\nÇıkmak için 'q'ya basınız")

bakiye = 0
while True:
    giris = input("Yapmak istediginiz islemi giriniz:")
    if(giris == "1"):
        yatTutar = int(input("Yatırmak istediginiz tutari giriniz:"))
        bakiye += yatTutar
    elif(giris == "2"):
        cekTutar = int(input("Cekmek istediginiz tutari giriniz"))
        if(cekTutar > bakiye):
            print("Bakiyenizde istediğiniz miktarda para bulunmamaktadir.Lutfen tekrardan deneyiniz")
            continue
        else:
            bakiye -= cekTutar
    elif(giris == "3"):
        print("Hesabinizde {} tl bulunmaktadir!".format(bakiye))
    elif(giris == "q"):
        print("Basariyla cikis yapildi!")
        break
    else:
        print("Geçersiz input,Lutfen tekrar deneyiniz!")

