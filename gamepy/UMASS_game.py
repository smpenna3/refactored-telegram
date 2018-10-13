import pygame
from pygame.locals import *

SCREENSIZE = 300

class Apple(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, pygame.sprite.RenderUpdates())
        self.x = x
        self.y = y

        self.image = pygame.image.load("apple.png")

    def drawScreen(self, screen):
        screen.blit(self.image, (self.x, self.y))

def main():
    pygame.init()
    screen = pygame.display.set_caption("apple")
    screen = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))

    apple = Apple(100, 100)


    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0

        keystate = pygame.key.get_pressed()


        apple.drawScreen(screen)
        pygame.display.flip()

        clock.tick(40)

    pygame.quit()


if __name__=="__main__":
    main()
