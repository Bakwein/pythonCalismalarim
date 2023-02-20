# ax^2+bx+c = 0

a = int(input("a\'i giriniz:"))
b = int(input("b\'yi giriniz:"))
c = int(input("c\'yi giriniz:"))

print("Olusan denklem ->", "{}x^2+ {}x+{} = 0" .format(a, b, c))
disc = (b ** 2)-(4 * a * c)

ilkKok = (-b + (disc ** 1/2)) / (2 * a)
digerKok = (-b - (disc ** 1/2)) / (2 * a)

print("Kokler -> {} / {}".format(ilkKok,digerKok))
