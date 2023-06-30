d1 = open("isimler1") # dosyayı açıyoruz
d1_satırlar = d1.readlines() # satırları okuyoruz
d2 = open("isimler2")
d2_satırlar = d2.readlines()

for a in d1_satırlar:
    if not a in d2_satırlar:
        print(a)

d1.close()
d2.close()