import pygame
from constants import *
from player import *
from circleshape import *

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
	Player.containers = (updatable_group, drawable_group)
	player = Player(x, y)

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

if __name__ == "__main__":
    main()
