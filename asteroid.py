import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_state, log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        ast1_velocity = self.velocity.rotate(angle)
        ast2_velocity = self.velocity.rotate(-angle)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid1.velocity = ast1_velocity * 1.2
        asteroid2.velocity = ast2_velocity * 1.2      