str = input("str:")
a = ""
for x in str:
    if x not in a:
        a += x
    else:
        continue
    print("{} harfinden str stringinde {} tane bulunmakta!".format(x,str.count(x)))
