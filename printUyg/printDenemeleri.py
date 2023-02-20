print("deneme", "sefa", "tunca", sep = '-')
print("sefa", "tunca",sep = None) # default gibi

print("sefa", "tunca", end = "\n") #default 
print("sefa","tunca",end = "-") #sefa tunca-
print("")
print("bir", "iki", "üç", "dört", "on dört", sep = " mumdur " , end = " mumdur\n")


dosya = open("deneme.txt","w")
print("Sefa Tunca!", file = dosya)
dosya.close() 
#deneme.txt dosyasına çıktı yazılır. deneme.txt dosyanın yerini bulmak için ise aşağıdaki çıktı izlenebilir. 

import os
print(os.getcwd()) #C:\Users\90506\Desktop

print(*"Sefa",sep = " ") #S e f a DEFAULT HALİ

print('O\'na söyledim!') # O'na söyledim! HATA YOK

print("Python 1990 yılında Guido Van Rossum \
tarafından geliştirilmeye başlanmış, oldukça \
 güçlü ve yetenekli bir programlama dilidir.")
print("")
print("Python 1990 yılında Guido Van Rossum " +
"tarafından geliştirilmeye başlanmış, oldukça " +
"güçlü ve yetenekli bir programlama dilidir.\n")

x = "Oyun simulasyonuna hoş geldiniz!"
print("-"*len(x), "\n", x , "\n", "-"*len(x), "\n", sep = "")

#open("C:\nisan\masraflar.txt") HATA
#open("C:\\nisan\masraflar") ÇÖZÜM1
#open("C:/nisan/masraflar") ÇÖZÜM2

print('google', '\b.', '\bcom', '\b.' ,'\btr' ) #google.com.tr BİTİŞİK


print(r"Kaçış dizileri: \, \n, \t, \a, \\, r")
