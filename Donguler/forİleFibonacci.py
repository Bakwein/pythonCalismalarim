print("Bulmak istediginiz aralıkları giriniz\n")
x = int(input("Baslangic->:"))
y = int(input("Son->:"))

a = 1
b = 1
fibonacci = [a, b]
for i in range(x, y+1):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)