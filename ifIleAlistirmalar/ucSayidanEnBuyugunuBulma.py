a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if(a > b and a > c):
    print(a)
elif(a > b and a < c):
    print(c)
elif(a < b and a > c):
    print(b)
elif(a < b and a< c):
    print(c)
else:
    print("karsilastirma yapilamiyor")