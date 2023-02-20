import math

print("XOX OYUNUNA HOŞ GELDİNİZ!")
print("Başlangıçta dizi aşağıdaki gibidir")
list = [["..(0)..", "..(1)..", "..(2).."],["..(3)..", "..(4)..", "..(5).."],["..(6)..", "..(7)..", "..(8).."]]
for i in list:
    print(*i)
print("")
print("İlk olarak X'ler başlar. Sonra sırayla devam eder.Kazanan olduğunda anında oyun biter!")
#KAZANAN OLMAYINCA OYUNU BAŞTAN BAŞLATMA
num = 0
secilen = None
secildi_mi = ""
is_number_true = 0
o_durumu = []
x_durumu = []
while True:
    #GİRİŞ BÖLÜMÜ
    print("Ne zaman çıkmak isterseniz q girmeniz yeterli!")
    if(num % 2 == 0):
        print("X'in turu!")
        secilen = input("Lütfen tabloya bakarak koymak istediğiniz bölümü seçiniz:")
        if(secilen == "q"):
            print("Cikis yapildi!")
            break
        while(is_number_true == 0):
            if(secilen in secildi_mi):
                print("Secilen numaralar(",secildi_mi,")'dan birini sectiniz!",sep = "")
                secilen = input("Lütfen secilen numaralar haricinde bir sayi giriniz:")
                if(secilen == "q"):
                    print("Cikis yapildi!")
                    break
            else:
                print("Sayı seçildi!")
                secildi_mi += secilen
                is_number_true = 1
    else:
        print("O'nun turu!")
        secilen = input("Lütfen tabloya bakarak koymak istediğiniz bölümü seçiniz:")
        if(secilen == "q"):
            print("Cikis yapildi!")
            break
        while(is_number_true == 0):
            if(secilen in secildi_mi):
                print("Secilen numaralar(",secildi_mi,")'dan birini sectiniz!",sep = "")
                secilen = input("Lütfen secilen numaralar haricinde bir sayi giriniz:")
                if(secilen == "q"):
                    print("Cikis yapildi!")
                    break
            else:
                print("Sayı seçildi!")
                secildi_mi += secilen
                is_number_true = 1
    #LİSTEYİ DEGİSTİRME
    a = math.floor(int(secilen) / 3)
    b = int(secilen) % 3
    if(num % 2 == 0):
        list[a][b] = "   X   "
        x_durumu += [[a, b]]
    else:
        list[a][b] = "   O   "
        o_durumu += [[a, b]]
    print("Liste başarıyla değiştirildi!")
    for i in list:
        print(*i)

    #KONTROL BÖLÜMÜ
    kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                        [[0, 1], [1, 1], [2, 1]],
                        [[0, 2], [1, 2], [2, 2]],
                        [[0, 0], [0, 1], [0, 2]],
                        [[1, 0], [1, 1], [1, 2]],
                        [[2, 0], [2, 1], [2, 2]],
                        [[0, 0], [1, 1], [2, 2]],
                        [[0, 2], [1, 1], [2, 0]]]
    for s in kazanma_ölçütleri:
        o = [z for z in s if z in o_durumu]
        x = [z for z in s if z in x_durumu]
        if len(o) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit()

    #DÖNGÜ SONU
    num += 1

