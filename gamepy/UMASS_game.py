import pygame
from pygame.locals import *


def main():
	pygame.init()
	
	image = pygame.image.load("apple.png")
	pygame.display.set_caption("apple")
	width = image.get_width()
	height = image.get_height()
	SIZE = 300

	imageX = (SIZE - width)/2
	imageY = (SIZE - height)/2
	angle = 0
	
	screen = pygame.display.set_mode((SIZE,SIZE))
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
			imageY -= 10
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
		if imageX > SIZE - width:
			imageX = SIZE - width
		if imageY < 0:
			imageY = 0   
		if imageY > SIZE - height:
			imageY = SIZE - height

		screen.blit(rotatedImage,(imageX, imageY))
			
		pygame.display.flip()
		
		imageY += 1
		
		clock.tick(40)
				
if __name__=="__main__":
	main()
