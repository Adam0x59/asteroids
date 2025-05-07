# Allows code from open-source pygame
# library to be used throughout this file
import pygame
from constants import *
from player import *

def main():

	# Initialisation
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	pygame.init()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	# Infinite Loop
	while True:

		# Check if game is still running
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		updatable.update(dt)
		for member in drawable:
			member.draw(screen)
		# player.draw(screen)
		# player.update(dt)
		# player.move(dt)
		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
