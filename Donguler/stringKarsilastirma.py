ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

"""
Siz burada, ilk_metin adlı değişken içinde bulunan, ama ikinci_metin adlı değişken içinde
bulunmayan öğeleri ayıklamak istiyorsunuz
"""
flag = 0
cevap = ""
for a in ilk_metin:
    flag = 0
    for b in ikinci_metin:
        if(a == b):
            flag += 1
    if flag == 0 and not a in cevap :
        cevap += a
print(cevap)