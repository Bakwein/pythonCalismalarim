liste2 = [ 2 , 4 ,8]
list1 = liste2
print(list1)
liste2[1] = "mehmet"
print(list1) #list1 de degisti

liste2 = [ 2 , 4 ,8]
liste4 = liste2[:]
liste2[0] = "a"
print(liste4) #DEGİSMEDİ

#VEYA

liste2 = [ 2 , 4 ,8]
liste3 = list(liste2)
liste2[1] = "x"
print(liste3) #DEGİSMEDİ