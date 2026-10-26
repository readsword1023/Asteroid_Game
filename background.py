import random
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PIXEL_SIZE

PIXEL = PIXEL_SIZE  # size of one "8-bit" pixel
STAR_COUNT = 140
TWINKLE_SECONDS = 0.6
SKY_COLOR = (4, 4, 16)
STAR_COLORS = [(255, 255, 255), (200, 220, 255), (255, 240, 180), (160, 180, 255)]


class Background:
    def __init__(self) -> None:
        # solid dark night sky
        self.sky = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.sky.fill(SKY_COLOR)

        # stars snapped to the pixel grid; some of them twinkle
        self.stars = []
        for _ in range(STAR_COUNT):
            x = random.randrange(0, SCREEN_WIDTH // PIXEL) * PIXEL
            y = random.randrange(0, SCREEN_HEIGHT // PIXEL) * PIXEL
            size = random.choice([PIXEL, PIXEL, PIXEL, PIXEL * 2])
            color = random.choice(STAR_COLORS)
            twinkle = random.random() < 0.4
            offset = random.uniform(0, TWINKLE_SECONDS)
            self.stars.append((x, y, size, color, twinkle, offset))

    def draw(self, screen) -> None:
        screen.blit(self.sky, (0, 0))
        now = pygame.time.get_ticks() / 1000
        for x, y, size, color, twinkle, offset in self.stars:
            if twinkle and int((now + offset) / TWINKLE_SECONDS) % 2 == 0:
                continue  # star is "off" this beat
            pygame.draw.rect(screen, color, (x, y, size, size))
            if size > PIXEL:
                # plus-shaped sparkle on the big stars
                pygame.draw.rect(screen, color, (x - PIXEL, y + PIXEL // 2, size + PIXEL * 2, PIXEL))
                pygame.draw.rect(screen, color, (x + PIXEL // 2, y - PIXEL, PIXEL, size + PIXEL * 2))
