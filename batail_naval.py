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

class ship:

   def __init__(self, name, positions):
       self.name= name
       self.positions= positions
       self.hit_position= set()
   def is_sunk(self):
       return all(pos in self.hit_positions for pos in self.positions)

   def attack(self, row, col):
       if (row, col) in self.positions:
           self.hit_positions.add((row, col))
           return True, f"Hit on {self.name}!"
       return False, "Miss!"


class battaleshipgame :
    def __init__(self, board_size, ships):
        self.board = Board(board_size)
        self.ships = {name: Ship(name, positions) for name, positions in ships.items()}
    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships.values())



