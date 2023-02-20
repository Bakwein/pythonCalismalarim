a = "İstanbul Büyükşehir Belediyesi"

print(a.split())

for i in a.split():
    print(i)
"""
x = input("Kısaltma için gerekli kelimeyi giriniz:")
for i in x.split():
    print(i[0],end = "")
print("")
"""
isimler = "Sefa,Ali,Mehmet,Veli"
print(isimler.split(","))
for i in isimler.split(","):
    print(i)
print(isimler.split("ğ")) #olmayan karakter verirsek normal şekilde çıktı olur
for i in isimler.split("ğ"):
    print(i)

abb = "Ankara Büyükşehir Belediyesi"
print(abb.split(" ", 1))
for i in abb.split(" ", 1):
    print(i)

# PARANTEZ İÇİNE INTEGER DEĞER VERİLEMEZ

import sys
sürüm = sys.version
print(sürüm.split()[0])