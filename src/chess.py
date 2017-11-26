#!/usr/bin/env python
"""
A game of chess that uses quantum rules, has pieces that move diagonally, and involves four players
"""
import fire
import pygame


class Chess:
    def __init__(self) -> None:
        self.board = self._generate_board()

    def draw_board(self):
        # TODO: Draw board
        pass

    def _generate_board(self, row_count: int = 8, column_count: int = 8):
        board = []
        # TODO: Create a list with the given row count containing a list with given column count
        # TODO: Initialize the board with the desired pieces
        return board


def start_game():
    pygame.init()
    # TODO: Begin game


def main():
    print('Starting game...')
    start_game()


if __name__ == '__main__':
    fire.Fire(main)
