import pygame
from playgrid import *
from Rectangle import *
from constants import *


class Player(Rectangle):
    def __init__(self, game_grid, initial_row, initial_column):
        width = 40
        height = 40
        colour = (50,150,50)
        starting_grid_vector = game_grid[initial_row][initial_column]
        start_x = starting_grid_vector.x
        start_y = starting_grid_vector.y
        super().__init__(start_x, start_y, width, height, colour)
        self.game_grid = game_grid
        self.initial_row = initial_row
        self.initial_column = initial_column
        

        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass