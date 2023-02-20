str = "sefaTunca"

for a in range(len(str)):
    print("Stringin ", a, ". harfi ->", " " , str[a],sep = "")
print("")
for a in range(len(str)):
    print("Stringin {}. harfi -> {}".format(a,str[a]))
print("")
for a in range(len(str)):
    print("Stringin {}. harfi -> {}".format(a+1,str[a]))