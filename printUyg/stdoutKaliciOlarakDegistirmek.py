import sys
f = open("degisim.txt", "w")
sys.stdout, f = f, sys.stdout
print("Dosya içine yazdık!", flush = True)
sys.stdout, f = f, sys.stdout
print("Terminal'de çıktı aldık!")