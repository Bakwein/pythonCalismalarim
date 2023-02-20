'''
class Araba():
    def __init__(self):
        print("Araba çağrıldı")

araba1 = Araba() #Araba çağrıldı
'''

class Araba():
    def __init__(self,model,renk,beygir_gucu,silindir):
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir

araba1 = Araba("Megane","Pembe",50,2)
print(araba1.silindir,araba1.beygir_gucu,araba1.renk,araba1.model)