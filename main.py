"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Karel Nechvatal
email: knechvatal6@seznam.cz
"""

# Konstanty
BOARD_SIZE = 3
PLAYER_SYMBOLS = ["O", "X"]
EMPTY_CELL = " "

# Úvodní zobrazení pravidel hry
def print_intro():
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 40)
    print("Let's start the game")
    print("-" * 40)

# Inicializace prázdného herního pole
def create_board():
    return [EMPTY_CELL] * 9

# Vykreslení hracího pole
def print_board(board):
    print("=" * 40)
    for i in range(0, 9, 3):
        print("+---+---+---+")
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
    print("+---+---+---+")
    print("=" * 40)

# Kontrola vstupu od hráče
def get_player_input(board, player_symbol):
    while True:
        try:
            move = input(f"Player {player_symbol} | Please enter your move number (1-9): ")
            position = int(move) - 1
            if position < 0 or position >= 9:
                print("Invalid move: Please choose a number from 1 to 9.")
            elif board[position] != EMPTY_CELL:
                print("Invalid move: This position is already taken.")
            else:
                return position
        except ValueError:
            print("Invalid input: Please enter a valid number from 1 to 9.")
2

# Vyhodnocení výhry
def check_win(board, symbol):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # řádky
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # sloupce
        [0, 4, 8], [2, 4, 6]             # diagonály
    ]
    for combo in win_combinations:
        if all(board[i] == symbol for i in combo):
            return True
    return False
