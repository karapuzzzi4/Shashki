#
#                           (/^▽^)/
#     ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
#   ////////👨‍💻KODA AUTORS : Maksims Bokijs(211RDB167)👨‍💻\\\\\\\\
#    ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                           (/^▽^)/
#


import pygame
from shashki.variables import long, high, size_of_field, grey, white
from shashki.game import Game
from min_max_algoritm.min_and_max_algoritm import minimax

FPS = 60

WIN = pygame.display.set_mode((long, high))


def get_row_col_from_mouse(pos):            ## get location of field by mouse
    x, y = pos
    row = y // size_of_field
    col = x // size_of_field
    return row, col


def main():                 ## main script for game
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == white:
            value, new_board = minimax(game.get_board(), 4, grey, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False
            main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
