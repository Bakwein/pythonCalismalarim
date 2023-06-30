dosyalar = ["/Users/sefatunca/Desktop/pythonCalismalarim/dosyaIslemleri/anaOrnekler/resimTurleri/giphy.gif",
            "/Users/sefatunca/Desktop/pythonCalismalarim/dosyaIslemleri/anaOrnekler/resimTurleri/foto1.jpg",
            "/Users/sefatunca/Desktop/pythonCalismalarim/dosyaIslemleri/anaOrnekler/resimTurleri/foto2.png"]


for f in dosyalar:
    okunan = open(f, 'rb').read(10)
    if okunan[6:11] in [b'JFIF', b'Exif']:
        print("{} adlı dosya bir JPEG!".format(f)) 
    elif okunan[:8] == b"\211PNG\r\n\032\n":
        print("{} adlı dosya bir PNG!".format(f)) 
    elif okunan[:3] == b'GIF':
        print("{} adlı dosya bir GIF!".format(f)) 
    elif okunan[:2] in [b'II', b'MM']:
        print("{} adlı dosya bir TIFF!".format(f)) 
    elif okunan[:2] in [b'BM']:
        print("{} adlı dosya bir BMP!".format(f)) 
    else:
        print("Türü bilinmeyen dosya: {}".format(f))