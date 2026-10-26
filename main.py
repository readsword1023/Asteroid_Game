from player import Player
from asteroid import Asteroid
from circleshape import CircleShape
from asteroidfield import AsteroidField
from shot import Shot
from background import Background
import pygame 
from constants import SCREEN_HEIGHT, SCREEN_WIDTH 
from logger import log_state, log_event
import sys

def show_game_over(screen, background, clock, score):
    title_font = pygame.font.Font(None, 96)
    score_font = pygame.font.Font(None, 64)
    hint_font = pygame.font.Font(None, 32)
    center_x = SCREEN_WIDTH // 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                return event.key == pygame.K_r
        background.draw(screen)
        title = title_font.render("GAME OVER", True, "red")
        final = score_font.render(f"Final Score: {score}", True, "white")
        hint = hint_font.render("Press R to restart  |  any other key to exit", True, "gray")
        screen.blit(title, (center_x - title.get_width() // 2, SCREEN_HEIGHT // 2 - 120))
        screen.blit(final, (center_x - final.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
        screen.blit(hint, (center_x - hint.get_width() // 2, SCREEN_HEIGHT // 2 + 60))
        pygame.display.flip()
        clock.tick(60)

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    background = Background()
    score = 0
    font = pygame.font.Font(None, 36)
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        background.draw(screen)

        updatable.update(dt)
        for asteroid in asteroids:
            if CircleShape.collides_with(player, asteroid):
                log_event("player_hit")
                print("Game over!")
                return show_game_over(screen, background, clock, score)
        for asteroid in asteroids:
            for shot in shots:
                if CircleShape.collides_with(shot, asteroid):
                    log_event("asteroid_shot")
                    score += asteroid.score_value()
                    asteroid.split()
                    shot.kill()

        for object in drawable:
            object.draw(screen)

        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    while main():
        pass
