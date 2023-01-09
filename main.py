import pygame
from game_class import Game


def main():
    game = Game()
    while game.run:
        game.clock.tick(60)
        game.handle_levels()
        game.handle_events()

    pygame.quit()


if __name__ == '__main__':
    main()
