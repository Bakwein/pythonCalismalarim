demet = ("ahmet", "mehmet", 23, 45)
print(demet)

print(tuple("abcdef"))
print(tuple(["ahmet", "mehmet", 34, 45])) # List->Tuple

#TANIMLAMA  
dem = ('ahmet')
print(type(dem)) #STR
dem1 = ('ahmet',)
dem2 = 'ahmet',
print(type(dem1), type(dem2)) #TUPLE

#DEMET ÖĞELERİNE ERİŞMEK
demet = ('elma', 'armut', 'kiraz')
print(demet[-1])
print(demet[:2])

#DEMET-LIST FARKI
# LISTELER DEĞİŞTİRİLEBİLİR(MUTABLE) İKEN DEMETLER DEĞİŞTİRİLEMEZLER(İMMUTABLE)

demet = ('elma', 'armut', 'kiraz')
#demet[0] = 'karpuz' HATAAA!
demet = demet + ('selin',) #DEMET EKLEME
print(demet)
#demet = demet + 'sefa' HATA 'sefa'->str

#in Python tabanlı bir web çatısı (framework)
#olan Django’nun settings.py adlı ayar dosyasında pek çok değer bir demet olarak saklanır.
#Mesela bir Django projesinde web sayfalarının şablonlarını (template) hangi dizin altında
#saklayacağınızı belirlediğiniz ayar şöyle görünür:
TEMPLATE_DIRS = ('/home/projects/djprojects/blog/templates',)#, ÖNEMLİ TEK ELEMANLI DEMET YARATILMAK İSTENİRSE KESİNLİKLE KULLANILMALIDIR. YOKSA STR OLARAK ALGILANIR!
