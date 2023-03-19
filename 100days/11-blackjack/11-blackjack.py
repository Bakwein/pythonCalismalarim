from art import logo
import random
import os

def choose1(cards, x,time):
    for a in range(time):
        x.append(random.choice(cards))

def total(x):
    toplam = 0
    for el in x:
        toplam += el
    return toplam

def ace_check(x):
    for el1 in x:
        if(el1 == 11):
            return True
    return False

def finish_message(user_cards,total_user,computer_cards,total_computer):
    print(f"Your cards: {user_cards} Current score: {total_user}")
    print(f"Computer's cards: {computer_cards} Computer's score:{total_computer}")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    global first_check
    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if(wanna_play == 'y'):
        os.system('clear')
        print(logo)
        user_cards = []
        computer_cards = []
        choose1(cards,user_cards,2)
        choose1(cards,computer_cards,2)
        def cont():
            total_user = total(user_cards)
            total_computer = total(computer_cards)
            print(f"Your cards: {user_cards} Current score: {total_user}")
            print(f"Computer's first card: {computer_cards[1]}")
            if(total_user == 21):
                if(len(computer_cards)):
                    finish_message(user_cards,total_user,computer_cards,total_computer)
                    print("You win!")
                    print("Win with a blackjack")
                    blackjack()
            elif(total_computer == 21):
                if(len(computer_cards)):
                    finish_message(user_cards,total_user,computer_cards,total_computer)
                    print("You lose")
                    print("Lost with a blackjack")
                    blackjack()
            if(total_user > 21):
                if(ace_check(user_cards)):
                    if(total_user -10 > 21):
                        finish_message(user_cards,total_user,computer_cards,total_computer)
                        print("You lose")
                        blackjack()
                else:
                    finish_message(user_cards,total_user,computer_cards,total_computer)
                    print("You lose")
                    blackjack()
            new_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if(new_card == 'y'):
                choose1(cards,user_cards,1)
                choose1(cards,computer_cards,1)
                total_user = total(user_cards)
                total_computer = total(computer_cards)
                cont()
            else:
                choose1(cards,computer_cards,1)
                total_computer = total(computer_cards)
                while(total_computer < 17):
                    choose1(cards,computer_cards,1)
                    total_computer = total(computer_cards)
                if(total_computer > 21):
                    finish_message(user_cards,total_user,computer_cards,total_computer)
                    print("You win!")
                    blackjack()
                else:
                    if(total_user > total_computer):
                        finish_message(user_cards,total_user,computer_cards,total_computer)
                        print("You win!")
                        blackjack()
                    elif(total_user < total_computer):
                        finish_message(user_cards,total_user,computer_cards,total_computer)
                        print("You lose")
                        blackjack()
                    else:
                        finish_message(user_cards,total_user,computer_cards,total_computer)
                        print("Draw!")
                        blackjack()
        cont()
    else:
        exit()
blackjack()







############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

