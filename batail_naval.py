#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Function to initialize the board
"""
Battleship game:
Battleship (also known as Battleships) is a strategy type guessing game for two players.
 It is played on ruled grids (paper or board) on which each player's fleet of warships are marked.
 The locations of the fleets are concealed from the other player.
 Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
"""
"""
class board = class of print board of gmae 
"""
class board :
    """

    method of create board
    Args:
        size (int): size of board game.
        grid (list): place of board


    """
    def __init__(self, size):
        self.size = size
        self.grid = [['-' for _ in range(size)] for _ in range(size)]
        self.attack_position= set()


   def display(self, reveal_ships=False):

      pass


def attack_position(self, row, col):
    if (row, col) in self.attacked_positions:
        print(f"It has been attacked already at ({row + 1}, {chr(col + 65)}). Please try again.")
        return False
    self.attacked_positions.add((row, col))
    return True


# Function to place ships on the board and track their positions
def position_ship(board, ships):
    ship_positions = {}
    for name, positions in ships.items():
        ship_positions[name] = set()
        for pos in positions:
            row, col = pos
            board[row][col] = 'S'
            ship_positions[name].add((row, col))
    return ship_positions


# Function to display the board
def print_board(board, reveal_ships=False):
    # Convert column index to letter
    print("  " + " ".join([chr(65 + i) for i in range(len(board))]))
    for idx, row in enumerate(board):
        if reveal_ships:
            print(f"{idx + 1} " + " ".join(cell if cell != 'S' else '*' for cell in row))
        else:
            print(f"{idx + 1} " + " ".join(cell if cell in ['X', 'O', '-'] else '-' for cell in row))


# Function to handle player's attack and check the state of the ship
def attack(board, row, col, ship_positions):
    if board[row][col] == "S":
        board[row][col] = "X"

        for name, positions in ship_positions.items():
            if (row, col) in positions:
                positions.remove((row, col))

                if not positions:
                    for row,col in ship_positions[name]:

                        board[row][col]='*'

                    return True, f"{name} is sunk!"
                else:
                    return True, f"{name} is hit!"
        return True, "Hit!"
    elif board[row][col] == "-":
        board[row][col] = "O"
        return False, "Miss!"
    else:
        return None, "Already attacked!"


# Function to check if all ships are sunk
def all_ships_sunk(ship_positions):
    return all(not positions for positions in ship_positions.values())


# Function to convert user input to board indices
def convert_position(pos):
    col = ord(pos[0].upper()) - 65
    row = int(pos[1:]) - 1
    return row, col


def play_game(board, ships, size):
    ship_positions = position_ship(board, ships)
    attacked = set()
    while True:
        print_board(board)
        try:
            move = input("Enter your move (ex., C2): ")
            if len(move) < 2 or not move[0].isalpha() or not move[1:].isdigit():
                raise ValueError("Invalid input format")

            row, col = convert_position(move)

            if not (0 <= row < size and 0 <= col < size):
                print(f"Invalid move. Coordinates must be within board size {size}. Please enter again.")
                continue

            if (row, col) in attacked:
                print(f"It has been attacked already at ({row + 1}, {chr(col + 65)}). Please try again.")
                continue

            attacked.add((row, col))
            result, message = attack(board, row, col, ship_positions)
            print(message)

            if all_ships_sunk(ship_positions):
                print_board(board, reveal_ships=True)
                print("All ships have been sunk! You win!")
                break

        except (ValueError, SyntaxError, NameError):
            print("Invalid input format. Please enter coordinates like C2.")


def main():
    ships = {
        'aircraft carrier': [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)],
        'cruiser': [(3, 0), (4, 0), (5, 0), (6, 0)],
        'destroyer': [(4, 2), (5, 2), (6, 2)],
        'submarine': [(4, 7), (4, 8), (4, 9)],
        'torpedo boat': [(8, 4), (8, 5)]
    }
    size = 10
    board = init_board(size)
    play_game(board, ships, size)


if __name__ == "__main__":
    main()
