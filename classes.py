import pygame
import random

# Defining the scale of the car
# Used by Player and Enemy classes
CAR_SCALE = (100, 150)

# Used to offset the top and bottom parts of the car from screen edge
OFFSET_CARS = 5

class MyClock:
    def __init__(self, fps) -> None:
        self.CLOCK = pygame.time.Clock()
        self.FPS = fps
    
    def tick(self) -> None:
        self.CLOCK.tick(self.FPS)

class BackgroundImage:
    def __init__(self, width, height) -> None:
        self.IMAGE = pygame.image.load('./img/road.png').convert_alpha()
        self.IMAGE = pygame.transform.scale(self.IMAGE, (width, height))
        self.HEIGHT = height
        self.movableY = 0
        self.SPEED = 4

    def draw(self, screen) -> None:
        screen.blit(self.IMAGE, (0, self.movableY))
        screen.blit(self.IMAGE, (0, -self.HEIGHT + self.movableY))
        self.movableY += self.SPEED

        if self.movableY > self.HEIGHT:
            self.movableY = 0

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.image = pygame.image.load('./img/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, CAR_SCALE)

        # Used to calculate what part of the image of the road can be driven on
        # and which can't be driven on
        percent = width * 0.2

        # Used to offset the top and bottom parts of the car from screen edge
        OFFSET_CARS = 5

        self.RIGHT_BORDER = width - percent
        self.LEFT_BORDER = percent
        self.TOP_BORDER = OFFSET_CARS
        self.BOTTOM_BORDER = height - OFFSET_CARS

        self.SPEED = 5
        
        self.rect = self.image.get_rect( bottomleft = (self.LEFT_BORDER, self.BOTTOM_BORDER) )

    def update(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.left -= self.SPEED
            if self.rect.left < self.LEFT_BORDER:
                self.rect.left = self.LEFT_BORDER
        if keys[pygame.K_d]:
            self.rect.right += self.SPEED
            if self.rect.right > self.RIGHT_BORDER:
                self.rect.right = self.RIGHT_BORDER
        if keys[pygame.K_s]:
            self.rect.bottom += self.SPEED
            if self.rect.bottom > self.BOTTOM_BORDER:
                self.rect.bottom = self.BOTTOM_BORDER
        if keys[pygame.K_w]:
            self.rect.top -= self.SPEED
            if self.rect.top < self.TOP_BORDER:
                self.rect.top = self.TOP_BORDER

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

class RandomEnemy(pygame.sprite.Sprite):
    def __init__(self, width) -> None:
        super().__init__()

        rng = random.choice([1, 2])

        self.image = pygame.image.load(f'./img/enemy_{rng}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, CAR_SCALE)

        # Used to calculate what part of the image of the road can be driven on
        # and which can't be driven on
        # Index 0 is for the cars in left track
        # The top point is 20% of the whole width
        # Index 1 is for the cars in the right track
        # The top point is the entire width - 40% of the entire width
        percent = [width * 0.2, width - width * 0.4]

        # Used to offset the top and bottom parts of the car from screen edge
        OFFSET_CARS = 5

        self.SPEED = 5

        self.rect = self.image.get_rect( topleft = (percent[rng - 1], OFFSET_CARS) )

    def update(self) -> None:
        self.rect.bottom += self.SPEED

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)