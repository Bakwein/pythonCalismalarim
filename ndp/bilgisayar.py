import time

class Bilgisayar:
    def __init__(self,model,alinisTarihi,fiyat,durum):
        self.model = model
        self.alinisTarihi = alinisTarihi
        self.fiyat = fiyat
        self.durum = durum

    def zam(self,zam):
        print("Zam geldi!")
        self.fiyat += zam
        print("Yeni fiyat->", self.fiyat)

    def indirim(self,indir):
        print("İndirim!")
        self.fiyat -= indir
        print("Yeni fiyat->", self.fiyat)
    
    def calistir(self):
        if(self.durum == 0):
            print("Bilgisayar acildi")
            self.durum = 1
    
    def kapat(self):
        if(self.durum == 1):
            print("Bilgisayar kapandi")
            self.durum = 0

    def guncelleme(self):
        if(self.durum == 1):
            print("Guncelleme baslatiliyor")
            time.sleep(2)
            print("Guncelleme tamamlandi,yeniden başlatılıyor!")
            self.kapat()
            self.calistir()
        elif(self.durum == 0):
            self.calistir()
            print("Guncelleme baslatiliyor")
            time.sleep(2)
            print("Guncelleme tamamlandi,yeniden başlatılıyor!")
            self.kapat()
            self.calistir()

    def __str__(self):
        print("Model->",self.model, "Alinis Tarihi->", self.alinisTarihi, "Fiyat->",self.fiyat,"Durum->",self.durum)


bilgi1 = Bilgisayar("3600","10.10.2022",10000,0)
bilgi1.calistir()
bilgi1.kapat()
bilgi1.guncelleme()
bilgi1.zam(1000)
bilgi1.__str__()
bilgi1.indirim(5000)
bilgi1.__str__()
bilgi1.kapat()
