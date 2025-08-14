import pygame

#base class for game objects
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        self.image = pygame.Surface((width,height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def draw(self, screen):
    # subclasses must override
        pass

    def update(self, dt):
    # subclasses must override
        pass









