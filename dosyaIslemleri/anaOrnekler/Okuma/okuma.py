#f = open("C:\\Users\\90506\\Desktop\\Github repolarim\\pythonCalismalarim\\dosyaIslemleri\\anaOrnekler\\Yazma\\deneme.txt","w")

#f = open("dosyaIslemleri\\anaOrnekler\\Yazma\\deneme.txt")

f = open("dosyaIslemleri\\anaOrnekler\\Yazma\\deneme.txt","r")
print(f.read())
#alt alta print yazıldığında yanlış çıkmasının nedeni bir kere print yazıldıktan sonra imlec sona geleceği okuyamaz
print()
f = open("dosyaIslemleri\\anaOrnekler\\Yazma\\deneme.txt","r")
print(f.readline())
print()
f = open("dosyaIslemleri\\anaOrnekler\\Yazma\\deneme.txt","r")
print(f.readlines())
