# REMOVE()

l = ["elma","kiraz","elma","uzum"]
print(l)
l.remove("elma")
print(l)
l.remove("elma")
print(l)

print("",end="\n\n")

#REVERSE()
meyveler = ["elma", "armut", "çilek", "kiraz"]
#meyveler[::-1]

#meyveler = reversed(meyveler) 
#print(meyveler) # <list_reverseiterator object at 0x000001CAAF18BFD0>

print(*reversed(meyveler))
print(list(reversed(meyveler)))

print()

for i in reversed(meyveler):
    print(i)

print()

xd = ["sefa",25,"tunca",23]
print(xd)
xd.reverse()
print(xd)
