sayac = 0
for i in dir(""):
    if "_" not in i[0]:
        sayac +=1
        print(sayac, ". " , i, sep = "")
print("Toplam {} tane metod var".format(sayac))
    
