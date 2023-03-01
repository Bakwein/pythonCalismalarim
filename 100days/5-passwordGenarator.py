#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""
#BASİT
passw = ""
for a in range(nr_letters):
    passw += random.choice(letters)

for b in range(nr_symbols):
    passw += random.choice(symbols)

for c in range(nr_numbers):
    passw += random.choice(numbers)

print(passw)
print("")

#shuffle(list)
#Verdiğiniz bir liste içindeki değerlerin sırasını karıştırır.

passw = list(passw)
print(passw)
random.shuffle(passw)
print(passw)
password = ""
for eleman in passw:
    password += eleman
print(password)

"""

password = ""
len = nr_letters + nr_symbols + nr_numbers
a = b = c = 0
while True:
    if(nr_letters != a or nr_symbols != b or nr_numbers != c):
        x = random.randint(0,2)
        if(x == 0 and nr_letters != a):
            password += random.choice(letters)
            a += 1
        elif(x == 1 and nr_symbols != b):
            password += random.choice(numbers)
            b += 1
        elif(x == 2 and nr_numbers != c):
            password += random.choice(symbols)
            c += 1
    else:
        break
print(password)



