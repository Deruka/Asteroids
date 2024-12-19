import pygame
import constants
import player
import asteroid
import asteroidfield
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    frames = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Shot.containers = (shots, drawable, updatable)
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    character = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    AsteroidField = asteroidfield.AsteroidField()
    dt = 0

    while True:
        dt = frames.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for one in asteroids:
            if one.collision(character) == True:
                print("Game over!")
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    main()
