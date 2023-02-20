birler = ["" , "bir", "iki", "üç", "dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

sayi = int(input("Sayi:"))
print(onlar[sayi // 10], birler[sayi % 10])