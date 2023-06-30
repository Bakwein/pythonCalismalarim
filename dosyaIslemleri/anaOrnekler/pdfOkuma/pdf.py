#/Users/sefatunca/Desktop/kouPdflerim/Fizik2/Soru\ Çözümü-3.pdf

f = open("/Users/sefatunca/Desktop/kouPdflerim/Fizik2/SoruCozumu.pdf", "rb")

okunan = f.read()
producer_index = okunan.index(b"/Producer")
#print(producer_index)
#print(chr(okunan[producer_index+11]))
producer = (okunan[producer_index:producer_index+50])

print(producer)