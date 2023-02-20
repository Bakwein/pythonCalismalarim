liste = [1, 2, 3, 4, 5, 6, 7]
tekToplam = 0
ciftToplam = 0

for eleman in liste:
    if(eleman % 2 == 0):
        ciftToplam += eleman
    else:
        tekToplam += eleman

print("Tek toplam -> {0}\nCift toplam -> {1}\nTümünün toplamı -> {2}" .format(tekToplam, ciftToplam,tekToplam+ciftToplam))