a = open("dosya.txt", encoding="utf-8")

for y in a:
    for x in y:
        print(x, end = "") #sep yapsan da geçersiz

a.close()
"""
sep fonksiyonu print fonksiyonunun bir parametresidir ve varsayılan olarak boşluk karakterini kullanır. Ancak, dosyalarda çıktı verirken print fonksiyonu, çıktıyı belirtilen dosyaya yazdırır ve sep parametresi etkisiz hale gelir. Dosyaya yazılan çıktılar genellikle bir satır sonu karakteri (\n) ile ayrılır. Eğer dosyaya yazılan çıktıları bir başka karakter ile ayırmak istiyorsanız, end parametresini kullanabilirsiniz.
"""