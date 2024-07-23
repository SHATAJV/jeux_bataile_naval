#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Function to initialize the board
"""
Battleship game:
Battleship (also known as Battleships) is a strategy type guessing game for two players.
 It is played on ruled grids (paper or board) on which each player's fleet of warships are marked.
 The locations of the fleets are concealed from the other player.
 Players alternate turns calling "shots" at the other player's ships,
  and the objective of the game is to destroy the opposing player's fleet.
"""
class Board:
    def __init__(self, size):
        """
        Initialize the board with the given size.

        :param size: Size of the board (size x size)
        """
        self.size = size
        self.grid = [['-' for _ in range(size)] for _ in range(size)]
        self.attacked_positions = set()

    def display(self, ships=None, reveal_ships=False):
        """
        Display the current state of the board.

        :param ships: Dictionary of ships to reveal their positions 
        :param reveal_ships: Boolean flag to reveal ship positions
        """
        # Print column headers
        print("  " + " ".join(chr(c) for c in range(65, 65 + self.size)))
        for row in range(self.size):
            # Print row header
            print(f"{row + 1:2}", end=" ")
            for col in range(self.size):
                if (row, col) in self.attacked_positions:
                    print(self.grid[row][col], end=' ')
                elif reveal_ships and ships and any((row, col) in ship.positions for ship in ships.values()):
                    print('S', end=' ')
                else:
                    print(self.grid[row][col], end=' ')
            print()
        print()

    def attack_position(self, row, col, hit):
        """
        Attack a position on the board.

        :param row: Row index
        :param col: Column index
        :param hit: True if the attack was a hit, False if it was a miss
        :return: True if the position was not previously attacked, False otherwise
        """
        if (row, col) in self.attacked_positions:
            print(f"It has been attacked already at ({row + 1}, {chr(col + 65)}). Please try again.")
            return False
        self.attacked_positions.add((row, col))
        self.grid[row][col] = 'X' if hit else 'O'
        return True


class Ship:
    def __init__(self, name, positions):
        """
        Initialize a ship with its name and positions.

        :param name: Name of the ship
        :param positions: List of positions occupied by the ship
        """
        self.name = name
        self.positions = positions
        self.hit_positions = set()

    def is_sunk(self):
        """
        Check if the ship is sunk.

        :return: True if the ship is sunk, False otherwise
        """
        return all(pos in self.hit_positions for pos in self.positions)

    def attack(self, row, col):
        """
        Attack a position on the ship.

        :param row: Row index
        :param col: Column index
        :return: Tuple (hit, message) where hit is True if the ship is hit, and message is the result message
        """
        if (row, col) in self.positions:
            self.hit_positions.add((row, col))
            if self.is_sunk():
                return True, f"{self.name} has been sunk"
            return True, f"Hit on {self.name}!"
        return False, "Miss!"


class BattleshipGame:
    def __init__(self, board_size, ships):
        """
        Initialize the Battleship game with a board and ships.

        :param board_size: Size of the board
        :param ships: Dictionary of ship names and their positions
        """
        self.board = Board(board_size)
        self.ships = {name: Ship(name, positions) for name, positions in ships.items()}

    def all_ships_sunk(self):
        """
        Check if all ships are sunk.

        :return: True if all ships are sunk, False otherwise
        """
        return all(ship.is_sunk() for ship in self.ships.values())

    def play(self):
        """
        Play the Battleship game. Handles user input and game loop.
        """
        while True:
            try:
                self.board.display(ships=self.ships, reveal_ships=False)
                coordinates = input("Enter attack coordinates (e.g., C2): ").strip()
                col = ord(coordinates[0].upper()) - 65
                row = int(coordinates[1:]) - 1

                hit_any_ship = False
                for ship in self.ships.values():
                    hit, message = ship.attack(row, col)
                    if hit:
                        hit_any_ship = True
                        print(message)
                        break

                if not self.board.attack_position(row, col, hit_any_ship):
                    continue

                if not hit_any_ship:
                    print("Miss!")

                if self.all_ships_sunk():
                    self.board.display(ships=self.ships, reveal_ships=True)
                    print("All ships have been sunk! You win!")
                    break
            except (ValueError, SyntaxError, NameError, IndexError):
                print("Invalid input format. Please enter coordinates like C2.")

def main():
    """
    Main function to set up and start the Battleship game.
    """
    ships = {
        'aircraft carrier': [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)],
        'cruiser': [(3, 0), (4, 0), (5, 0), (6, 0)],
        'destroyer': [(4, 2), (5, 2), (6, 2)],
        'submarine': [(4, 7), (4, 8), (4, 9)],
        'torpedo boat': [(8, 4), (8, 5)]
    }
    game = BattleshipGame(board_size=10, ships=ships)
    game.play()

if __name__ == "__main__":

    main()

