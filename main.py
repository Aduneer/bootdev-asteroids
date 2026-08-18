import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0


    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # instantiate player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # event loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update all updatable obj with dt
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        # draw all drawable obj on screen
        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

        

if __name__ == "__main__":
    main()
