from player import Player
from asteroid import Asteroid
from circleshape import CircleShape
from asteroidfield import AsteroidField
from shot import Shot
import pygame 
from constants import SCREEN_HEIGHT, SCREEN_WIDTH 
from logger import log_state, log_event
import sys

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
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

        updatable.update(dt)
        for asteroid in asteroids:
            if CircleShape.collides_with(player, asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if CircleShape.collides_with(shot, asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
