import pygame
from constants import *

def generate_grid():
    grid_array = []
    for row in range(16):
        current_row_cells = []
        for col in range(16):
            centre_x = 0 + (CELL_WIDTH * col) + (CELL_WIDTH/2)
            centre_y = SCREEN_HEIGHT - (CELL_HEIGHT * row) - (CELL_HEIGHT/2)
            current_row_cells.append(pygame.Vector2(centre_x, centre_y))
        grid_array.append(current_row_cells)
    return grid_array
