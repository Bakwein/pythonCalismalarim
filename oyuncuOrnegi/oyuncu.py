print("Oyuncunun bilgileri\n")


ad = input("Oyuncunun adini giriniz:")
soyad = input("Oyuncunun soyadini giriniz:")
yas = int(input("Oyuncunun yasini giriniz:"))

bilgiler = [ad,soyad,yas]

print("Oyuncunun adi-> {}\nOyuncunun soyadi-> {} \nOyuncunun yasi-> {}\n ".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Oyuncunun adi-> {}\n" .format(bilgiler[0]),"Oyuncunun soyadi-> {} \n" .format(bilgiler[1]),"Oyuncunun yasi-> {}\n ".format(bilgiler[2]))
