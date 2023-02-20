"""
a = int(input("1. sayiyi giriniz:"))
b = int(input("2. sayiyi giriniz:"))
c = int(input("3. sayiyi giriniz:"))

print("{} * {} * {} = {}" .format(a, b, c, a*b*c))
"""


"""
boy = float(input("Metre cinsinden boyunuzu giriniz:"))
kilo = int(input("Kilonuzu giriniz:"))

# bke = kilo / (boy ** 2)
print("Boyunuz: {} \nKilonuz: {} \nKitle İndeksiniz: {} \n".format(boy, kilo, kilo / (boy ** 2)))
"""

"""
kmBasinaYakilan = int(input("Kilometre basina yakilan miktari L cinsinden giriniz:"))
kacKm = int(input("Kac kilometre yapildigini giriniz:"))
neKadar = int(input("Yakitin Litresinin ne kadar olduğunu giriniz:"))

print("Yapilan Km -> {}\nKm Basina Yakilan Miktar -> {}\nOdenecek tutar -> {}".format(kacKm, kmBasinaYakilan, kacKm * kmBasinaYakilan * neKadar))
"""


"""
ilkSayi = int(input("1. sayiyi giriniz:"))
digerSayi = int(input("2. sayiyi giriniz:"))
sonSayi = int(input("3. sayiyi giriniz:"))
print("ilk -> {} diger -> {} son -> {}" .format(ilkSayi,digerSayi,sonSayi))
ilkSayi,digerSayi,sonSayi = sonSayi,ilkSayi,digerSayi
#ilkSayi,digerSayi,sonSayi = sonSayi,ilkSayi,ilkSayi ONCEKİ DEGERİNİ VERİR SWAPTE VERİLEN DEGER ONEMSIZ
print("ilk -> {} diger -> {} son -> {}" .format(ilkSayi,digerSayi,sonSayi))
"""

"""
ilkKenar = int(input("ilk kenari giriniz:"))
ikinciKenar = int(input("ikinci kenari giriniz:"))

c = (ilkKenar ** 2) + (ikinciKenar ** 2)
print("Diger kenar ->",c)
c = (c ** 0.5)
"""


a = 9 ** 0.5
b = 9 ** 1/2
print(a, b)



