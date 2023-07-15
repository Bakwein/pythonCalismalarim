tel_no = {
    "ahmet": "0532 532 32 32",
    "mehmet": "0533 533 33 33",
    "ayşe": "0534 534 34 34",
    "fatma": "0535 535 35 35",
    "hayriye": "0536 536 36 36",
    "hüseyin": "0537 537 37 37",
}

x = input("Lutfen telefon numarasini istediginiz kisinin ismini giriniz: ")

if x in tel_no:
    cevap = "{} kisinin telefon numarasi {}"
    print(cevap.format(x,tel_no[x]))
else:
    print("Bu kisinin ismi listede yok")