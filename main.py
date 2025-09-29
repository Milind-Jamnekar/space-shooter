# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroidfield import AsteroidField
from constants import *

from astroid import Asteroid
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
