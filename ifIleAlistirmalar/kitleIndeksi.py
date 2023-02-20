kilo = float(input("Kilonuzu giriniz(kg):"))
boy = float(input("Boyunuzu giriniz(m):"))

kitleIndeksi = kilo / (boy ** 2)
if(kitleIndeksi < 18.5):
    print("Zayif")
elif(kitleIndeksi >= 18.5 and kitleIndeksi < 25):
    print("Normal")
elif(kitleIndeksi >= 25 and kitleIndeksi < 30):
    print("Fazla kilolu")
elif(kitleIndeksi >= 30):
    print("Obez")