'''
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

*İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.*
'''

for a in range(1,11):
    print("**************************************")
    for b in range(1,11):
        print("{} x {} = {} ".format(a, b, a * b))
