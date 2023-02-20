isim = "sefa"
print("Benim adım %s" %(isim))

print("%s ve %s iyi bir ikilidir" %("Python", "Django"))
#%s -> karakter dizisi tutmada kullanılır
#içerideki %s ile dışarıdaki sayı tutmazsa hata verir

for i in range(3):
    print("%s" %i)
#yüzde sayısı çift olursa hata verir tek yüzdeyı çıktı alabilemek için aşağıdaki gibi kullanmamız gerekir
for i in range(3):
    print("%%%s" %i)

print("|%15s|" %"deneme")  #|         deneme|
print("|%-15s|" %"deneme") #|deneme         |

print("%(ürün)s deposunda %(miktar)s kilo %(ürün)s var" %{"miktar": 35, "ürün" : "elma"})

#%s -> string
#%d -> sayılar
#%i -> integer
#%o -> octal
#%x %X -> dexadecimal
#%f -> float
#%c -> char(int -> char / char->int değişimleri olabilir)
print("Ben %d yaşındayım" %15)
print("Ben %s yaşındayım" %15) #HATA OLMAZ ama tam dersinde HATA OLUR
print("%d" %13.5) #13
print("%s" %13.5) #13.5
print("|%7d|" %22)
print("|%-7d|" %22)
print("%05d" %23)
print("%.5d" %23)
print("%10.5d" %23) #10 boşlukta 5 boyutlu olacak şekilde 0 ekleyerek sağa doğru yapışık  şekilde yazdırır
print("%10.d" %23)
print("%010.d" %23)

print("%f" %10)
print("%.2f" %10,end ="\n\n")

for i in range(20):
    print("%(deger)5d %(deger)5o %(deger)5x %(deger)5X" %{"deger" : i})