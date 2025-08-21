import pygame

#base class for game objects
class Rectangle(pygame.sprite.Sprite):
    def __init__(self,x, y, width, height, colour):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.width = width
        self.height = height
        self.colour = colour
        self.position = pygame.Vector2(x, y)
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self, screen):
    # subclasses must override
        pass

    def update(self, dt):
    # subclasses must override
        pass









