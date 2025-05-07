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
		player.draw(screen)
		pygame.display.flip()player.draw(screen)
		dt = clock.tick(60)

if __name__ == "__main__":
	main()
