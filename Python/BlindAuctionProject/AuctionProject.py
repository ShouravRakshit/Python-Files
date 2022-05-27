from art import logo
from os import system, name

print(logo)

dict = {

}
print("Welcome to the secret auction program")

# Created a function that can clean the terminal.
def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

# Populating the dictionary.
def populate_dict():
    userInput = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    dict[userInput] = bid

# Finding the winner of the auction.
def auction_winner():
    highest = 0
    winner_name = ""
    for key in dict:
        if dict[key] > highest:
            highest = dict[key]
            winner_name = key

    print(f"The winner is {winner_name} with a bid of ${highest}.")


populate_dict()
while True:
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if other_bidder == 'yes':
        clear()
        populate_dict()
    elif other_bidder == 'no':
        auction_winner()
        break
    else:
        print("Wrong choice!")