from art import logo
import os
print(logo)


dict = {}
higher_bid = 0
higher_name = None
while True:
    name = input("What is your name?: ")
    bid = int(input("Please enter your bid: $"))
    dict[name] = bid
    if(dict[name] > higher_bid):
        higher_bid = dict[name]
        higher_name = name
    another = input("Are there any other bidders?(yes/no):")
    if(another == "yes"):
        os.system('clear')
    else:
        print(f"The winner is {higher_name} with a bid ${higher_bid}.")
        break




    