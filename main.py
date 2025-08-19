import pygame
from Rectangle import *
from constants import *

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameclock = pygame.time.Clock()
    dt = 0
    square = Rectangle((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2),50,50,(50,150,50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(square.image, square.rect)
        pygame.display.flip()
        dt = gameclock.tick(60) / 1000


if __name__ == "__main__":
    main()
