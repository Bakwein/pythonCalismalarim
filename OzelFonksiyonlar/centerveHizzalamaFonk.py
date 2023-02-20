a = "merhaba"
#ortalamak için kullanılır
print(a.center(3))
print(a.center(10))
print(a.center(10, "-"))

#sağa yaslama -> rjust() 
#sola yaslama-> ljust()
for i in dir(""):
    print(i.ljust(20))
for i in dir(""):
    print(i.rjust(20))

x = "tel no"
print(x.ljust(10, "."))
