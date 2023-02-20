vize1 = int(input("vize1:"))
vize2 = int(input("vize2:"))
final = int(input("final:"))

ortalama = (vize1*30/100) + (vize2*30/100) + (final*40/100)
if(ortalama >= 90):
    print("AA")
elif(ortalama >= 85):
    print("BA")
elif(ortalama >= 80):
    print("BB")
elif(ortalama >= 75):
    print("CB")
elif(ortalama >= 70):
    print("CC")
elif(ortalama >= 65):
    print("DC")
elif(ortalama >= 60):
    print("DD")
elif(ortalama >= 55):
    print("FD")
elif(ortalama < 55):
    print("FF")