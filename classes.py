import pygame

# Defining the scale of the car
# Used by Player and Enemy classes
CAR_SCALE = (100, 150)

class MyClock:
    def __init__(self, fps) -> None:
        self.CLOCK = pygame.time.Clock()
        self.FPS = fps
    
    def tick(self) -> None:
        self.CLOCK.tick(self.FPS)

class BackgroundImage:
    def __init__(self, width, height, path) -> None:
        self.IMAGE = pygame.image.load(path).convert_alpha()
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
    def __init__(self, width, height, path) -> None:
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, CAR_SCALE)

        # Used to calculate what part of the image of the road can be driven on
        # and which can't be driven on
        percent = width * 0.2

        # Used to offset the top and bottom parts of the car from screen edge
        offset = 5

        self.RIGHT_BORDER = width - percent
        self.LEFT_BORDER = percent
        self.TOP_BORDER = offset
        self.BOTTOM_BORDER = height - offset

        self.SPEED = 4

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

