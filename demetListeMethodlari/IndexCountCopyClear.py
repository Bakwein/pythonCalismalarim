# INDEX VE COUNT

liste = ["elma", "armut", "çilek","elma"]
print(liste.index("elma")) # 0
#print(liste.index("")) # olmayan bir şeyi sorarsak hata verir
print(liste.count("elma")) # 2

#Copy()
liste1 = ["ahmet", "mehmet", "özlem"]
liste2 = liste1[:]
liste2 = list(liste1)
liste2 = liste1.copy()

liste.clear()
print(liste) #[]

