import pygame, sys
import numpy as np
pygame.init()
wight = 600
height = 600
line_width = 15
board_rows = 3
board_cols = 3
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55
red = (15, 255, 255)
bg_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)
white = (32, 50, 52)
color=(255, 255, 255)
screen = pygame.display.set_mode((wight, height))
pygame.display.set_caption("khaled and tasneem tic tac toe")
screen.fill(bg_color)
board = np.zeros((board_rows, board_cols))
print(board)


def draw_line():
    pygame.draw.line(screen, line_color, (0, 200), (600, 200), line_width)
    pygame.draw.line(screen, line_color, (0, 400), (600, 400), line_width)
    pygame.draw.line(screen, line_color, (200, 0), (200, 600), line_width)
    pygame.draw.line(screen, line_color, (400, 0), (400, 600), line_width)


def draw_figures():
    for row in range(board_rows):
        for cal in range(board_cols):
            if board[row][cal] == 1:
                pygame.draw.circle(screen, red, (int(cal*200+100), int(row*200+100)), circle_radius, circle_width)
            elif board[row][cal] == 2:
                pygame.draw.line(screen, white, (cal*200+space, row*200+200-space), (cal*200+200-space, row*200+space), cross_width)
                pygame.draw.line(screen, white, (cal*200+space, row*200+space), (cal*200+200-space, row*200+200-space), cross_width)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False



def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    for row in range(board_rows):
        if board[0][row] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    posx = col * 200 + 100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (posx, 15), (posx, height-15), 15)


def draw_horizontal_winning_line(row, player):
    posy = row * 200 + 100

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, posy), (wight-15, posy), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, height-15), (wight - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, 15), (wight - 15, height - 15), 15)


def restart():
    screen.fill(bg_color)
    draw_line()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0


draw_line()
player = 1
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY//200)
            clicked_col = int(mouseX//200)
            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over=False

    pygame.display.update()
