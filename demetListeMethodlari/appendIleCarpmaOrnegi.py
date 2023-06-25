'''
sonuc = 1

while True:
    x = input("Bir sayi giriniz:(cikmak icin 'q')")
    if(x == 'q'):
        break
    sonuc *= int(x)

print("sonuc:",sonuc)
'''

# SAYI GİRİLMEYİP DİREKT Q İLE ÇIKIŞ YAPILIRSA 1 DÖNDÜRÜR BİZ BUNU ENGELLEMEK İÇİN LİSTELER KULLANABİLİRİZ

sonuc = 1
l = []
while True:
    x = input("Bir sayi giriniz:(cikmak icin 'q')")
    if(x == 'q'):
        break
    l.append(x)

if(len(l) < 2):
    print("Yeterli sayi girilmedi")
else:
    for i in l:
        sonuc *= int(i)
    print("sonuc:",sonuc)