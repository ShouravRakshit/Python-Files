from tkinter import *
import random


def display_board():
    print(f"{board[0]}" + " |" + f" {board[1]}" + " | " + f"{board[2]}")
    print(f"{board[3]}" + " |" + f" {board[4]}" + " | " + f"{board[5]}")
    print(f"{board[6]}" + " |" + f" {board[7]}" + " | " + f"{board[8]}")


def play_game(player):

    display_board()
    position = (input(f"Give me a position (1-9) player {player}"))
    board[int(position) - 1] = "X"


board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
while True:
    if play_game() == "sad":
        print("Game Over!")
        break
