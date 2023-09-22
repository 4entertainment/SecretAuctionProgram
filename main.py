import os
from art import logo


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo + "Welcome to the Secret Auction Program.\n")
flag = False

auction_dictionary = {}
max_bid = 0

while not flag:
    name = input("What is your name?:")
    bid = int(input("What's your bid?: $"))

    auction_dictionary[name] = bid

    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if choice == "yes":
        clear_screen()
    else:
        flag = True

for key in auction_dictionary:
    if auction_dictionary[key] > max_bid:
        max_bid = auction_dictionary[key]
        winner = key

clear_screen()
print(f"The winner is {winner} with a bid of ${max_bid}")



