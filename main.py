import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, width, height, title) -> None:
        pygame.init()

        self.WIDTH = width
        self.HEIGHT = height
        self.SCREEN = pygame.display.set_mode((width, height))
        
        pygame.display.set_caption(title)

        self.CLOCK = MyClock(60)

        self.BACKGROUND = BackgroundImage(width, height)

        self.PLAYER = Player(width, height)

        self.enemyGroup = pygame.sprite.Group()
        self.enemySpawnTime = 2000
        self.enemyCurrentSpawnTime = 0

    def quit(self) -> None:
        pygame.quit()
        exit()
    
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            self.BACKGROUND.draw(self.SCREEN)

            self.PLAYER.update()
            self.PLAYER.draw(self.SCREEN)

            if pygame.time.get_ticks() - self.enemyCurrentSpawnTime >= self.enemySpawnTime:
                self.enemyGroup.add( RandomEnemy(self.WIDTH, self.HEIGHT) )
                self.enemyCurrentSpawnTime = pygame.time.get_ticks()

            self.enemyGroup.update()
            self.enemyGroup.draw(self.SCREEN)

            collision = pygame.sprite.spritecollide(self.PLAYER, self.enemyGroup, False)

            if collision:
                self.quit()

            pygame.display.update()
            self.CLOCK.tick()
            

if __name__ == '__main__':
    game = Game(600, 800, 'Point Collector')
    game.run()
