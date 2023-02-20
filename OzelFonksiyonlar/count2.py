parola = input("parola:")
flag = 0
for a in parola:
    if parola.count(a) > 1:
        flag += 1

if flag > 0:
    print("Aynı karakteri birden fazla kullanamazsınız")
else:
    print("Sifreniz onaylandi!")