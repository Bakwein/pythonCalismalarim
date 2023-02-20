def pisa():
    l = list()
    for a in range(1,101):
        for b in range(1,101):
            c = (a ** 2 + b ** 2) ** 0.5
            if(c == int(c)):
                l.append((a,b,int(c)))
    return l

print(pisa())
