'''
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
'''

a = int(input("Sayiyi giriniz:"))
s = 0
for x in range(1, a):
    if(a % x == 0):
        s += x

if(a == s):
    print(a, " bir mükemmel sayidir")
else:
    print(a, " bir mükemmel sayi degildir")
