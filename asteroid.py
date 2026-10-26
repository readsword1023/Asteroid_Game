import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, ASTEROID_MIN_RADIUS, SCORE_LARGE_ASTEROID, SCORE_MEDIUM_ASTEROID, SCORE_SMALL_ASTEROID
from logger import log_state, log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 

    def score_value(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return SCORE_SMALL_ASTEROID
        elif self.radius <= ASTEROID_MIN_RADIUS * 2:
            return SCORE_MEDIUM_ASTEROID
        return SCORE_LARGE_ASTEROID

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