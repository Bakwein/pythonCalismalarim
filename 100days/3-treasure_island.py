print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road_choose = input("""You're at a cross road. Where do you want to go? Type "left" or "right" """)
road_choose = road_choose.lower()
left_choice = wait_choice = color_choice = None
if(road_choose == "left"):
    left_choice = input("""You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across """)
    left_choice = left_choice.lower()
    if(left_choice == "wait"):
        color_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        color_choice = color_choice.lower()
        if(color_choice == "red"):
            print("You burned by fire")
            print("Game Over.")
        elif(color_choice == "yellow"):
            print("You Win!")
        elif(color_choice == "blue"):
            print("You were eaten by beasts")
            print("Game Over.")
        else:
            print("Game Over.")
    else:
        print("You were attacked by trout.")
        print("Game Over.")
else:
    print("You fell into a hole.")
    print("Game Over.")
