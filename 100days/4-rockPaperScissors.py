rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

x = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if(x >= 3 or x < 0):
    print("User entered wrong number!")
else:
    y = random.randint(0,2)
    print(f"Computer chose {y}")
    list1 = [rock,paper,scissors]
    print("You chose:")
    print(list1[x])
    print("Computer chose:")
    print(list1[y])
    if(x == y):
        print("DRAW!")
    elif((x == 0 and y == 1) or (x == 2 and y == 0) or (x == 1 and y == 2)):
        print("COMPUTER WON!")
    elif((x == 0 and y == 2) or (x == 1 and y == 0) or (x == 2 and y == 1) ):
        print("YOU WON!")

