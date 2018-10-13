import random, os.path
import pygame
from pygame.locals import *
import logging, traceback, time, datetime


SCREENRECT = Rect(0, 0, 1280, 720)


# Data directory make sure it exists
data_directory = 'teldata'
if not os.path.exists(data_directory):
	os.makedirs(data_directory)
	
	
# Functions for opening single or multiple images
def load_image(file):
	file = os.path.join(data_directory, file)
	try:
		surface = pygame.image.load(file)
	except:
		print(traceback.print_exc())
		raise SystemExit()
	return surface.convert()
	
def load_images(*files):
	imgs = []
	for file in files:
		imgs.append(load_image(file))
	return imgs
	

	
'''
	PLAYER CLASS
'''
class Player(pygame.sprite.Sprite):
	# Global variables
	speed = 5
	bounce = 10
	images = []
	
	# Initialize the class
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
		self.reloading = 0
		self.origtop = self.rect.top
		self.facing = -1
		
	def move(self, direction):
		self.rect.move_ip(direction*self.speed, 0)
		self.rect = self.rect.clamp(SCREENRECT)
		if direction < 0:
			self.image = self.images[0]
		else:
			self.image = self.images[1]
		self.rect.top = self.origtop - (self.rect.left//self.bounce%2)
		

# Main 		
def main():
	pygame.init()
	pygame.mixer = None # no sound
	
	# Display mode
	winstyle = 0
	bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
	screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
	
	# Create the player
	img = load_image('mario.gif')
	Player.images = [pygame.transform.flip(img, 1, 0), img]
	
	# Create the background
	back = load_image('level.gif')
	background = pygame.Surface(SCREENRECT.size)
	for x in range(0, SCREENRECT.width, back.get_width()):
		background.blit(back, (x, 0))
	screen.blit(background, (0, 0))
	pygame.display.flip()
	
	# Go
	all = pygame.sprite.RenderUpdates()
	Player.containers = all
	
	# Create a player
	player = Player()
	
	clock = pygame.time.Clock()
	
	while(1):
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				return
		keystate = pygame.key.get_pressed()
		
		all.clear(screen, background)
		all.update()
		
		direction = keystate[K_RIGHT] - keystate[K_LEFT]
		player.move(direction)
		dirty = all.draw(screen)
		pygame.display.update(dirty)
		
		
		clock.tick(40)
		
	pygame.quit()
		
		
# Run main 
if __name__ == '__main__':
	main()