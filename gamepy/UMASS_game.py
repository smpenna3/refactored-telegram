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


def main():
	pygame.init()
	
	image = pygame.image.load("apple.png")
	pygame.display.set_caption("apple")
	width = image.get_width()
	height = image.get_height()
	SIZE = 300

	imageX = (SIZE - width)/2
	imageY = (80)
	angle = 0
	
	# Velocity
	velocityG = 0
	AG = 15
	
	screen = pygame.display.set_mode((SIZE,900))
	screen.blit(image,(imageX, imageY))
	pygame.display.flip()
	
	clock = pygame.time.Clock()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return 0

		keystate = pygame.key.get_pressed()

		if keystate[K_RIGHT]:
			imageX += 10
		elif keystate[K_LEFT]:
			imageX -= 10
		elif keystate[K_UP]:
			velocityG = 0
			imageY -= 100
		elif keystate[K_DOWN]:
			imageY += 10
		elif keystate[K_r]:
			angle += 10
		elif keystate[K_l]:
			angle -= 10

		screen.fill((0,0,0))

		originalCenter = image.get_rect().center
		rotatedImage = pygame.transform.rotate(image, angle)
		rotatedImage.get_rect().center = originalCenter

		if imageX < 0:
			imageX = 0
		elif imageX > SIZE - width:
			imageX = SIZE - width
		if imageY < 0:
			imageY = 0   
		elif imageY > 880 - height:
			imageY = 900 - height
			velocityG = 0
		else:
			velocityG += AG
			imageY += velocityG * (1/40)

		screen.blit(rotatedImage,(imageX, imageY))
			
		pygame.display.flip()
		
		logger.debug(velocityG)
		
		clock.tick(40)
				
if __name__=="__main__":
	main()
