# APPEND()

liste = ["ali","veli"]
print(liste)
liste.append(23)
print(liste)
#liste.append(45,55) #denilemez tek eleman alır HATA

print()

l = [1,2,3]
print(l)
for i in [4,5,6]:
    l.append(i)
print(l)

print()

l1 = [1,2,3]
print(l1)
l1.append([4,5,6])
print(l1)

print()
# EXTEND()

l2 = [4,5,6]
l3 = [7,8,9]
print(l2)
l2.extend(l3)
print(l2)



