import pygame
from pygame.locals import *
import time, logging

# Setup logging
formatter = logging.Formatter('%(asctime)s - [%(levelname)7s]. - %(message)s')
logger = logging.getLogger('mainlog')
logger.setLevel(logging.DEBUG)
#fh = logging.handlers.RotatingFileHandler('log.log', maxBytes=5*1024*1024, backupCount=10)
#fh.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
#logger.addHandler(fh)

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
