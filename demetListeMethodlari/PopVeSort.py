#pop()

liste = ["elma", "armut", "çilek"]
a=liste.pop()
print(a)
b=liste.pop(0)
print(b)
print(liste)

print("",end="\n\n")
#sort()

üyeler = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep',
'Abdullah', 'Kadir', 'Kemal', 'Kamil', 'Selin', 'Senem',
'Sinem', 'Tayfun', 'Tuna', 'Tolga']
üyeler.sort()
print(üyeler)
print()
üyeler.sort(reverse=True)
print(üyeler)
print("",end="\n\n")
sayılar = [1, 0, -1, 4, 10, 3, 6]
sayılar.sort()
print(sayılar)
sayılar.sort(reverse=True)
print(sayılar)
print("",end="\n\n")

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {harf: harfler.index(harf) for harf in harfler}
isimler = ["ahmet", "ışık", "ismail", "çiğdem", "can", "şule"]
isimler.sort(key=lambda x: çevrim.get(x[0]))
print(isimler)