import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	fps_clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	updatable_group = pygame.sprite.Group()
	drawable_group = pygame.sprite.Group()
	asteroid_group = pygame.sprite.Group()
	shot_group = pygame.sprite.Group()
	Shot.containers = (updatable_group, drawable_group, shot_group)
	AsteroidField.containers = (updatable_group)
	Asteroid.containers = (updatable_group, drawable_group, asteroid_group)
	Player.containers = (updatable_group, drawable_group)
	player = Player(x, y)
	astroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return

		screen.fill("black")

		for drawable in drawable_group:
			drawable.draw(screen)

		pygame.display.flip()
		dt = fps_clock.tick(60) / 1000
		updatable_group.update(dt)

		for asteroid in asteroid_group:
			if player.collision(asteroid):
				exit("Game Over!")

		for asteroid in asteroid_group:
			for shot in shot_group:
				if shot.collision(asteroid):
					shot.kill()
					asteroid.kill()

if __name__ == "__main__":
    main()
