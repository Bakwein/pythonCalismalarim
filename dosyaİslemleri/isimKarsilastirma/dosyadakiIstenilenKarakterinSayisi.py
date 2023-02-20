hakkinda = open("isimler1", encoding="utf-8")

harf = input("Sayisini ogrenmek istediginiz harfi giriniz:")

sayi = 0
for a in hakkinda:
    for b in a:
        if b == harf:
            sayi += 1
print(sayi)
