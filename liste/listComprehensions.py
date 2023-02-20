liste = [i for i in range(1000)]
print(liste)

liste1 = [i for i in range(1000) if i % 2 == 0]
print(liste1)

liste3 = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12]]

tum = [z for i in liste3 for z in i]
print(tum)