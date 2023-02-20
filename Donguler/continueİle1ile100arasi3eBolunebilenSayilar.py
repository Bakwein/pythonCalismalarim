'''
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi *continue* ile yapmaya çalışın.
'''

for a in range(1,101):
    if(a % 3 != 0):
        continue
    print(a)