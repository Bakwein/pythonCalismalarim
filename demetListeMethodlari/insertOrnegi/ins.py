f = open("demetListeMethodlari\\insertOrnegi\\deneme.txt","r")

okunan = f.readlines()
print(okunan)
okunan.insert(1,"Sefa Tunca\n")

f1 = open("demetListeMethodlari\\insertOrnegi\\deneme.txt","w")
f1.writelines(okunan)

f.close()
f1.close()
