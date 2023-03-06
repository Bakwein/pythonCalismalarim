from art import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    text = list(text)
    s = 0
    if(direction == "decode"):
      shift *= -1
    for a in text:
        x = alphabet.index(a)
        x += shift
        if (x > 25):
            x -= 26
        elif (x < 0):
            x += 26
        text[s] = alphabet[x]
        s += 1
    ans = ""
    for t in text:
        ans += t
    print(f"The {direction} text is {ans}")

while True:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26
  caesar(text, shift, direction=direction)
  q = input("Do you want to restart your program?(yes/no):")
  if q == "no":
    print("Thank you for using my program. Bye!")
    break
  elif q == "yes":
    os.system('clear')

'''
def encrypt(text, shift):
    text = list(text)
    s = 0
    for a in text:
        x = alphabet.index(a)
        x += shift
        if (x > 25):
            x = x - 26
        text[s] = alphabet[x]
        s += 1
    ans = ""
    for t in text:
        ans += t
    print(f"The encoded text is {ans}")

def decrypt(text, shift):
  text = list(text)
  s = 0
  for a in text:
      x = alphabet.index(a)
      x -= shift
      if (x < 0):
          x = x + 26
      text[s] = alphabet[x]
      s += 1
  ans = ""
  for t in text:
      ans += t
  print(f"The decoded text is {ans}")

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if (direction == "encode"):
    encrypt(text, shift)
elif(direction == "decode"):
  decrypt(text, shift)
'''
