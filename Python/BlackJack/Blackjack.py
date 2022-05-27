import random
from art import logo
from os import system, name


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

# Created a function that can clean the terminal.
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def remaining_cards(additional_cards, cards, turn):
    for card in range(1):
        additional_cards.append(random.choice(cards))

    card_total = sum(additional_cards)

    if turn == "p":
        print(f"Your cards: {additional_cards}, current score: {card_total}")

    elif turn == "c":
        print(f"Computer's first card: {additional_cards[0]}")

    return additional_cards


def firstTwoCards(cards, turn):
    card_list = []
    for card in range(2):
        card_list.append(random.choice(cards))

    if turn == "p":
        print(f"Your cards: {card_list}, current score {sum(card_list)}")
        # return card_list

    elif turn == "c":
        print(f"Computer's first card: {card_list[0]}")

    return card_list


def Blackjack():
    # decision = input("Do you want to play a game of black jack. Type 'y' for yes or 'n' for no ")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(logo)
    player_cards = firstTwoCards(cards, "p")
    comp_cards = firstTwoCards(cards, "c")
    comp_cards_value = sum(comp_cards)
    player_cards_value = sum(player_cards)

    # if decision == "y":
    while True:

        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        # Getting a another card after typing 'y'.
        if get_another_card == "y":
            player_remaining_cards = remaining_cards(player_cards, cards, "p")
            player_cards = player_remaining_cards  # Updating the list for the player.
            player_cards_value = sum(player_remaining_cards)  # Changing the value of the player_cards_value.
            if player_cards_value > 21:
                print(f"Your final hand: {player_cards}, final score: {player_cards_value}")
                print(f"Computer's final hand: {comp_cards}, final score: {comp_cards_value}")
                print("You went over. You lose.")
                break

        elif get_another_card == "n":
            # Dealer is going to take card until he has 17 or more points.
            while comp_cards_value < 17:
                comp_remaining_cards = remaining_cards(comp_cards, cards, "c")
                comp_cards = comp_remaining_cards  # Updating the list for the dealer.
                comp_cards_value = sum(comp_remaining_cards)  # Changing the value of the comp_cards_value.
                print(comp_cards)

            if player_cards_value < comp_cards_value < 22:
                print(f"Your final hand: {player_cards}, final score: {player_cards_value}")
                print(f"Computer's final hand: {comp_cards}, final score: {comp_cards_value}")
                print("Computer has a better hand than you")
                break

            elif comp_cards_value < player_cards_value < 22:
                print("You won")
                break

            elif comp_cards_value == player_cards_value:
                print("Draw")
                break

            elif comp_cards_value > 21:
                print("You won")
                break


decision = input("Do you want to play a game of black jack. Type 'y' for yes or 'n' for no ")
if decision == "y":
    Blackjack()
elif decision == "n":
    print("Sayonara")

while True:
    userInput = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if userInput == 'y':
        clear()
        Blackjack()
    elif userInput == 'n':
        print("Sayonara")
        break
