notlar = {}
print(type(notlar))
print(notlar)

print("")

notlar["Ahmet"] =21
print(notlar) # {'Ahmet': 21}
notlar["Veli"] = 50
print(notlar) #{'Ahmet': 21, 'Veli': 50}
notlar["Deniz"] = 95
notlar["Ege"] = 95
notlar["Zeynep"] = 100
print(notlar)

print("")

notlar["Ahmet"] = 90
print(notlar) # {'Ahmet': 90, 'Veli': 50, 'Deniz': 95, 'Ege': 95, 'Zeynep': 100}