'''
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

*İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.*
'''
cevap = 0

while True:
    a = input("Giriş(Sayı veya q):")
    if(a == "q"):
        print(cevap)
        break
    else:
        a = int(a)
        cevap += a
        print("Sonuc: ", cevap)

