from tic_tac_toe import run as tic_tac
from guessing_game import guessing_game

user_input = ''

while user_input != "exit":
    print("Game 1: Number Guessing Game\nGame 2: Tic-Tac-Toe")
    user_input = input("Game 1 or Game 2? ")

    if user_input == "1" or user_input == "Game 1":
        guessing_game()
    elif user_input == "2" or user_input == "Game 2":
        tic_tac()
