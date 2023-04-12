#
#                           (/^▽^)/
#     ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
#   ////////👨‍💻KODA AUTORS : Maksims Bokijs(211RDB167)👨‍💻\\\\\\\\
#    ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                           (/^▽^)/
#

import pygame
from .variables import grey, white, blue, size_of_field
from shashki.board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):           ##update game
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = grey
        self.valid_moves = {}

    def winner(self):               ## winner
        return self.board.winner()

    def reset(self):                    ##reset board and game
        self._init()

    def select(self, row, col):            ### select field
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):              ## make move
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):          ## draw valid  moves
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, blue,
                               (col * size_of_field + size_of_field // 2, row * size_of_field + size_of_field // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == grey:
            self.turn = white
        else:
            self.turn = grey

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()