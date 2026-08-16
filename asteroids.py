from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        rotated_vector_1 = self.velocity.rotate(angle)
        rotated_vector_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_1.velocity = 1.2 * rotated_vector_1
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_2.velocity = 1.2 * rotated_vector_2
