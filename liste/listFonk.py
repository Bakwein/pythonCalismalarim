alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
harf_listesi = list(alfabe)
print(harf_listesi)

print("")

li = list()
print(li)
print(list(range(10)))

meyveler = ["elma", "armut", "çilek", "kiraz"]

for a in range(len(meyveler)):
    print("{}. eleman -> {}".format(a,meyveler[a]))
print(" ") #veya
for a,b in enumerate(meyveler,0):
    print("{}. eleman -> {}".format(a,b))

print(meyveler[-2])
print(meyveler[:2])
meyveler = meyveler[::-1]
print(meyveler)
sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]
for a in range(len(sayılar)):
    for b in range(len(sayılar[a])):
        print("{} {} -> {}".format(a,b,sayılar[a][b]))
