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
"""
class board = class of print board of game
"""


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['~' for _ in range(size)] for _ in range(size)]
        self.attacked_positions = set()

    def display(self, ships=None, reveal_ships=False):

        for row in range(self.size):
            for col in range(self.size):
                if (row, col) in self.attacked_positions:
                    print('x')
                elif reveal_ships and ships and any((row, col) in ships.positions for ships in ships.values()):
                    print('S')
                else:
                    print(self.grid, end='')

    def attack_position(self, row, col):
        if (row, col) in self.attacked_positions:
            print(f"It has been attacked already at ({row + 1}, {chr(col + 65)}). Please try again.")
            return False
        self.attacked_positions.add((row, col))
        return True


class Ship:
    def __init__(self, name, positions):
        self.name = name
        self.positions = positions
        self.hit_positions = set()

    def is_sunk(self):
        return all(pos in self.hit_positions for pos in self.positions)

    def attack(self, row, col):
        if (row, col) in self.positions:
            self.hit_positions.add((row, col))
            return True, f"Hit on {self.name}!"
        return False, "Miss!"


class BattleshipGame:
    def __init__(self, board_size, ships):
        self.board = Board(board_size)
        self.ships = {name: Ship(name, positions) for name, positions in ships.items()}

    def all_ships_sunk(self):
        return all(ships.is_sunk() for ships in self.ships.values())

    def play(self):
        while True:
            try:
                coordinates = input("Enter attack coordinates (e.g., C2): ").strip()
                col = ord(coordinates[0].upper()) - 65
                row = int(coordinates[1:]) - 1

                if not self.board.attack_position(row, col):
                    continue

                hit_any_ship = False
                for ships in self.ships.values():
                    hit, message = ships.attack(row, col)
                    if hit:
                        hit_any_ship = True
                        print(message)
                        break

                if not hit_any_ship:
                    print("Miss!")
                    self.board.display(ships=self.ships, reveal_ships=False)

                if self.all_ships_sunk():
                    self.board.display(reveal_ships=True)
                    print("All ships have been sunk! You win!")
                    self.board.display(ships=self.ships, reveal_ships=False)
                    break
            except (ValueError, SyntaxError, NameError, IndexError):
                print("Invalid input format. Please enter coordinates like C2.")


def main():
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
