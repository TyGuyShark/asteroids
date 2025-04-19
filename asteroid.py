import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		random_angle = random.uniform(20,50)
		split_v1 = self.velocity.rotate(random_angle)
		split_v2 = self.velocity.rotate(-random_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		new_a1 = Asteroid(self.position[0], self.position[1], new_radius)
		new_a2 = Asteroid(self.position[0], self.position[1], new_radius)
		new_a1.velocity = split_v1 * 1.2
		new_a2.velocity = split_v2 * 1.2
