from object_classes import RedBird
import pygame
from window import Window
from levels import levels
from handle_bird_movement import (
    BIRD_DIED,
    ROUND_LOST,
    ROUND_WON,
)


class Game:
    '''
    Class Game is the class responsible for events and loading levels
    into the game loop.
    It`s created with params:
    -bird - RedBird class object;
    -window - Window class object;
    -clock - pygame clock object;
    -game_stage - indicates on which stage the game currently is; type: int
    -set_params - its a variable that indicates when player is setting
    the bird parameters before launch of the bird; type: int
    -number_of_tries - variable that indicates how many tries
    (launches of the bird) player has; type: int
    - run - game loop boolean variable

    '''
    def __init__(self):
        self.bird = RedBird()
        self.window = Window()
        self.clock = pygame.time.Clock()
        self.game_stage = 0
        self.set_params = 1
        self.number_of_tries = 20
        self.run = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN and self.set_params == 1:
                if event.key == pygame.K_SPACE:
                    self.set_params = 0
                    self.start_time = pygame.time.get_ticks()
                self.bird.set_params(event)
            if event.type == BIRD_DIED:
                self.set_params = 1
                self.number_of_tries -= 1
            if event.type == ROUND_LOST:
                self.run = False
                self.window.draw_loser()
            if event.type == ROUND_WON and self.game_stage == 4:
                self.bird.kill()
                self.run = False
                self.window.draw_winner()
            if event.type == ROUND_WON:
                self.game_stage += 1
                self.set_params = 1
                self.number_of_tries = 20
                self.bird.reset()

    def handle_levels(self):
        for level in levels:
            if level.level == self.game_stage:
                if self.set_params == 0:
                    time = (pygame.time.get_ticks() - self.start_time)/60
                    self.bird.movement(level, time, self.number_of_tries)
                else:
                    time = 0
                self.window.draw_window(self.bird, level,
                                        self.number_of_tries, time)
