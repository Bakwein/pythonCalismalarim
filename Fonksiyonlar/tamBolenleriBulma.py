'''
def bolenler(x):
    print(x, " Bolenleri:")
    for a in range(1,x):
        if(x % a == 0):
            print(a, end= ",")
    print(x)
'''

def bolenler(x):
    tam_bolenler = []
    for a in range(1,x+1):
        if(x % a == 0):
            tam_bolenler.append(a)
    print(tam_bolenler)

while True:
    sayi = input("Sayi(Çıkış için q):")
    if(sayi == "q"):
        break
    bolenler(int(sayi))