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
