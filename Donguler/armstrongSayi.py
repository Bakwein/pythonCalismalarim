'''
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
'''

a = int(input("Sayi:"))
sayi = a
basamak_sayisi = len(str(a))
toplam = 0
while(sayi > 0):
    c = sayi % 10
    toplam += (c ** basamak_sayisi)
    sayi = sayi // 10 #ONEMLI
    print(sayi)

if(basamak_sayisi == 4 and toplam == a):
    print(a, " bir armstrong sayidir")
else:
    print(a, " bir armstrong sayisi degil")