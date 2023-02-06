import pygame

class MyClock:
    def __init__(self, fps) -> None:
        self.CLOCK = pygame.time.Clock()
        self.FPS = fps
    
    def tick(self):
        self.CLOCK.tick(self.FPS)

class BackgroundImage:
    def __init__(self, width, height, path) -> None:
        self.IMAGE = pygame.image.load(path).convert_alpha()
        self.IMAGE = pygame.transform.scale(self.IMAGE, (width, height))
        self.HEIGHT = height
        self.movableY = 0
        self.SPEED = 2

    def draw(self, screen):
        screen.blit(self.IMAGE, (0, self.movableY))
        screen.blit(self.IMAGE, (0, -self.HEIGHT + self.movableY))
        self.movableY += self.SPEED

        if self.movableY > self.HEIGHT:
            self.movableY = 0