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
class board = class of print board of gmae 
"""


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['~' for _ in range(size)] for _ in range(size)]
        self.attacked_positions = set()

    def display(self, reveal_ships=False):
        # Logique pour afficher le plateau
        pass

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
        return all(ship.is_sunk() for ship in self.ships.values())

    def play(self):
        while True:
            try:
                coordinates = input("Enter attack coordinates (e.g., C2): ").strip()
                col = ord(coordinates[0].upper()) - 65
                row = int(coordinates[1:]) - 1

                if not self.board.attack_position(row, col):
                    continue

                hit_any_ship = False
                for ship in self.ships.values():
                    hit, message = ship.attack(row, col)
                    if hit:
                        hit_any_ship = True
                        print(message)
                        break

                if not hit_any_ship:
                    print("Miss!")

                if self.all_ships_sunk():
                    self.board.display(reveal_ships=True)
                    print("All ships have been sunk! You win!")
                    break
            except (ValueError, SyntaxError, NameError, IndexError):
                print("Invalid input format. Please enter coordinates like C2.")


