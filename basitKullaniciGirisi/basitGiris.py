sys_kullanici_adi = "stunca"
sys_sifre = "1234"

ka = input("Lutfen kullanici adinizi giriniz:")
sifre = input("Lutfen sifrenizi giriniz:")

if(ka == sys_kullanici_adi and sifre == sys_sifre):
    print("Basariyla giris yapildi!")
elif(ka == sys_kullanici_adi and sifre != sys_sifre):
    print("Hatali sifre girdiniz!")
elif(ka != sys_kullanici_adi and sifre == sys_sifre):
    print("Hatali kullanici adi girdiniz!")
else:
    print("Hatali kullanici adi ve sifre girdiniz")