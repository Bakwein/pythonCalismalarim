liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]
print(type(liste), end = "\n\n")

for a in liste:
    print("{} öğesinin tipi {}".format(a,type(a)))

print(liste[1])
print(len(liste))

sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]
for i in sayılar:
    print(*range(*i))