from game_data import data
from art import vs
from art import logo
import random
from os import system, name


# Created a function that can clean the terminal.
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def game():
    point = 0
    A = random.choice(data)

    while True:
        print(logo)
        if point > 0:
            print(f"You're right! Current score: {point}.")

        B = random.choice(data)
        a_follower = A["follower_count"]
        b_follower = B["follower_count"]

        if a_follower == b_follower:
            B = random.choice(data)

        print(a_follower)
        print(b_follower)

        print(f"Compare A: {A['name']} a {A['description']} from {A['country']}")
        print(vs)
        print(f"Against B: {B['name']} a {B['description']} from {B['country']}")

        user_input = input("Who has more followers? Type 'A' or 'B': ")

        if user_input == "A" and a_follower > b_follower:
            A = B  # Swaps the value of B to A for the next interation.

            point = point + 1
            clear()
        elif user_input == "B" and b_follower > a_follower:
            A = B  # Swaps the value of B to A for the next interation.

            point = point + 1
            clear()

        else:
            print(f"Sorry, that's wrong. Final score: {point}")
            return False


game()
