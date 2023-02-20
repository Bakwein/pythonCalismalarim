liste = [1, 2, 3]
liste[0:len(liste)] = 5, 6, 7
print(liste)

#ÖĞE EKLEME
list1 = [2,4,6]
#list1 = list1 + 5 HATA 
list1 = list1 + [5]
print(list1)

l2 = [1,2,3,9]
l3 = [5,6,7]
l4 = l2 + l3
print(l4)

sayilar = 0
notlar = []

for x in range(10):
    deger = int(input("Notu giriniz:"))
    sayilar += deger
    notlar += [deger]

print("Girilen notlar ->", notlar)
print("Not ortalamasi ->",sayilar/10)

notlar = []
for i in range(10):
    veri = input("{} . not: ".format(i+1))
    notlar += list(veri)
print("Girdiğiniz notlar: ", *notlar)   

#LİSTEDEN ÖGE CİKARMA
liste8 = [1, 5,3 ,2]
del liste8[-1]
print(liste8) # [1, 5, 3]

#LİSTEYİ SİLME
liste10 = [1,5,9,15]
print(liste10)
del liste #listeyi siler