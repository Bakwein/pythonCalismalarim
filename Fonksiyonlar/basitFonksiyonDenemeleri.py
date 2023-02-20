def selamla():
    print("Merhaba")
    print("Hosgeldin")

selamla()

def selamla(isim):
    print("Merhaba ",isim,", Nasılsın?")

selamla("Sefa") #Merhaba  Sefa , Nasılsın?
selamla(41.8) #Merhaba  41.8 , Nasılsın?

def faktoryel(sayi):
    faktoryel = 1
    if(sayi == 0 or sayi == 1):
        print("Faktoryel:",faktoryel)
    elif(sayi < 0):
        print("Sayi negatif, faktoryeli olamaz")
    else:
        while(sayi >= 1):
            faktoryel *= sayi
            sayi -= 1
        print("Faktoryel:",faktoryel)

faktoryel(5) #Faktoryel: 120
faktoryel(0) #Faktoryel: 1
faktoryel(-4) #Sayi negatif, faktoryeli olamaz


def toplama(a, b, c):
    print("Toplamları->",a+b+c)

toplama(2,-5,9) #Toplamları-> 6
#toplama(2,4,"sefa") HATA