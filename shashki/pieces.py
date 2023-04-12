#
#                           (/^▽^)/
#     ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
#   ////////👨‍💻KODA AUTORS : Maksims Bokijs(211RDB167)👨‍💻\\\\\\\\
#    ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                           (/^▽^)/
#
#
from .variables import  white, size_of_field, grey, crown_of_queen
import pygame


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):                             ## calculate position
        self.x = size_of_field * self.col + size_of_field // 2
        self.y = size_of_field * self.row + size_of_field // 2

    def make_king(self):                ### make king figure
        self.king = True

    def draw(self, win):                ### draw
        radius = size_of_field // 2 - self.PADDING
        pygame.draw.circle(win, grey, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(crown_of_queen, (self.x - crown_of_queen.get_width() // 2, self.y - crown_of_queen.get_height() // 2))

    def move(self, row, col):       ### make move
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)