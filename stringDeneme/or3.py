site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])
    print("flag")

for isim in site1, site2, site3, site4:
    print(isim[:-4] + "." + isim[-3:] + ".tr")