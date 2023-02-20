print("|{:>15}|" .format("deneme")) #sağa kaydırma
print("|{:<15}|" .format("deneme")) #sola    "
print("|{:^15}|" .format("deneme")) #ortalama

#%s -> string
#%b -> binary
#%c,%d,%o,%x,%X,%f
print("{:s}".format("string"))

for i in range(20):
    print("{:x} {:10X}".format(i, i))

print("{:,}".format(6545645656)) #basamak ayıracı