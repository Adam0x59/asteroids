# Allows code from open-source pygame
# library to be used throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():

	# Initialisation
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
	pygame.init()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots,updatable, drawable)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroid_field = AsteroidField()

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
		for asteroid in asteroids:
			if asteroid.circ_collision_check(player):
				print("Game over!")
				sys.exit(0)
			for shot in shots:
				if shot.circ_collision_check(asteroid):
					shot.kill()
					asteroid.split()
			

		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
