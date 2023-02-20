"""
LOWER
"""
a = "ELMA"
print(a.lower()) #elma
a = a.lower()
print(a) #elma
b = "arMUT"
print(b.lower()) #armut
c = "sefa"
print(c.lower()) #sefa
"""
x = "İSTANBUL"
print(x.lower()) İ harfinden dolayı hata!
"""
print("I".lower()) #i
iller = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"
iller = iller.replace("I", "ı").replace("İ","i").lower()
print(iller) #ısparta, adıyaman, diyarbakır, aydın, balıkesir, ağrı

""""
UPPER
"""
k = "kalem"
print(k.upper()) #KALEM
k1 = "istanbul"
print(k1.upper()) #ISTANBUL
iller1 = "istanbul, izmir, siirt, mersin"
print(iller1.replace("i", "I").upper()) #ISTANBUL, IZMIR, SIIRT, MERSIN
