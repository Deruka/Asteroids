# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    frames = pygame.time.Clock()
    character = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        character.draw(screen)
        pygame.display.flip()
        frames.tick(60)
        dt = frames.tick(60) / 1000


if __name__ == "__main__":
    main()
