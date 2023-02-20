
sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesliler = ""   
sessizler = ""

str = input("Kelime:")

for i in str:
        if i in sesli_harfler:
            sesliler += i
        elif i in sessiz_harfler:
            sessizler += i

print("Sessizler ->",sessizler)
print("Sesliler ->", sesliler)