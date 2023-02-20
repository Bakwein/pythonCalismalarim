sekil = input("sekilinizi yaziniz(Ucgen veya Dikdortgen):")

if(sekil == "Dortgen"):
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    if(a == b and b == c and c == d):
        print("Kare")
    elif((a == c and b == d) or (a == b and c == d) or (a == d and b == c)):
        print("Dikdortgen")
    else:
        print("Dortgen")
elif(sekil == "Ucgen"):
    e = int(input("e:"))
    f = int(input("f:"))
    g = int(input("g:"))
    if((abs(f-g) < e and e < f +g ) and (abs(e-f) < g and g < f +e ) and (abs(e-g) < f and f < g +e )):
        if(e == f and f == g):
            print("Eskenar")
        elif((e == f and f != g) or (e != f and f == g) or (e == g and g != f)):
            print("İkizkenar")
        elif(e != f and e != g and f != g):
            print("Cesitkenar")
    else:
        print("Ucgen belirtmiyor")
else:
    print("Gecersiz sekil")