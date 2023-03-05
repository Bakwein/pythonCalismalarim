import os
import random
from hangman_art import logo
from hangman_art import stages

error = len(stages) - 1
end_game = 0
print(logo)
print("Welcome to the hang-a-man game!")
print("It's player1's turn. Dont show this part to player2!")
word = input("Type a word for player2 to guess:").lower()
print(word)
word_list = []
a = len(word)
while(a > 0):
    word_list += list("_")
    a -= 1
os.system('clear')
print(logo)
print("Player1's turn is done. Now it's player2's turn! Good Luck *_*")

control = 0
already_did = ""
while(end_game != 1):
    print(f"If you make {error} mistakes, the game over.")
    for sefa in word_list:
        print(sefa + " ",end = "")
    print(stages[error])
    
    letter = input("Type a letter:").lower()
    while(len(letter) != 1):
        print("Your input's length must be 1")
        letter = input("Type a letter:").lower()
    
    word_set = 0
    while(word_set == 0 and letter in word): 
        x1 = 0
        for s in already_did:
            if(letter == s):
                print("You did this guess before")
                letter = input("Type a letter:").lower()
                #eğer already did'i girersek sorun görmüyor len checklemek lazim
                while(len(letter) != 1):      
                    print("Your input's length must be 1")
                    letter = input("Type a letter:").lower()
                x1 += 1
                break
        if(x1 == 0):
            already_did += letter
            word_set = 1
    x = 0
    is_guess_right = 0
    for let in word:
        if let == letter:
            word_list[x] = letter
            control += 1
            is_guess_right += 1
        x += 1
    os.system('clear')
    print(logo)
    if(is_guess_right > 0):
        print("Your guess is right :)")
    else:
        print("Your guess is not right :(")
        error -= 1

        #CONTROL
    if(len(word) == control):
        end_game = 1
        print("\nYou won!")
    elif(error == 0):
        end_game = 1
        print("\nYou lost")
print(stages[error])
print(f"The word was -> {word}")
