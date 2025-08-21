import pygame
from Rectangle import *
from constants import *
from player import *
from playgrid import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameclock = pygame.time.Clock()
        self.game_grid = generate_grid()
        self.player = Player(self.game_grid, 0, 8)


    def run(self):
        running = True
        dt = 0
        while running:
            dt = self.gameclock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.player.update()
            self.screen.fill((0,0,0))
            self.player.draw(self.screen)    
            pygame.display.flip()
            

if __name__ == "__main__":
    game = Game()
    game.run()