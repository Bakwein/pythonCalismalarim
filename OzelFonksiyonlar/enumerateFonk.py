print(*enumerate("sefaTunca"))
# 2 parametereli çıktı veriyor
for sıra,metod in enumerate(dir("")):
    print(metod, sıra)

for sıra,harf in enumerate("sefaTunca",1): #1'den başlatma
    print(sıra,harf)