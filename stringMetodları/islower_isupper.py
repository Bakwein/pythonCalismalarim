a = "sefa"
print(a.islower()) #True
b = "Icardi"
print(b.islower()) #False
"""
c = 32
print(c.islower()) HATA INT SORGULANAMAZ
"""
d = "32"
print(d.islower()) #False
print(d.isupper()) #False
e = "SEFA"
print(e.isupper()) #True
f = "SEFA41"
print(f.isupper()) #True
g = "S1"
print(f.isupper(),f.islower()) #True False
h = "s1"
print(h.islower(),h.isupper()) #True False