ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

"""
Siz burada, ilk_metin adlı değişken içinde bulunan, ama ikinci_metin adlı değişken içinde
bulunmayan öğeleri ayıklamak istiyorsunuz
"""
flag = 0
for a in ilk_metin:
    for b in ikinci_metin:
        if(a == b):
            flag += 1
    if flag == 0:
        print(a)


