#
#                           (/^▽^)/
#     ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
#   ////////👨‍💻KODA AUTORS : Maksims Bokijs(211RDB167)👨‍💻\\\\\\\\
#    ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                           (/^▽^)/
#
import pygame
from .variables import black, rowss, grey, blue, size_of_field, columns, white
from .pieces import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):                    ###make squares
        win.fill(black)
        for row in range(rowss):
            for col in range(row % 2, columns, 2):
                pygame.draw.rect(win, white, (row * size_of_field, col * size_of_field, size_of_field, size_of_field))

    def evaluate(self):             ##evaluation
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self, color):       ### get all pieces of board
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):        ## moves on board
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == rowss - 1 or row == 0:
            piece.king()
            if piece.color == white:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):          ## get cell
        return self.board[row][col]

    def create_board(self):                 ### creating board
        for row in range(rowss):
            self.board.append([])
            for col in range(columns):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, white))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, grey))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):                   ## draw
        self.draw_squares(win)
        for row in range(rowss):
            for col in range(columns):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):               ## remove figure
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == grey:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):                   ###winner
        if self.red_left <= 0:
            return white
        elif self.white_left <= 0:
            return grey

        return None

    def get_valid_moves(self, piece):          ## bad moves
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == grey or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == white or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, rowss), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, rowss), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):   ### kill left
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rowss)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]): #### kill right
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= columns:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rowss)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves