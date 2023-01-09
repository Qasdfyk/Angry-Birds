import pygame
import os
import math
pygame.font.init()

WIDTH, HEIGHT = 1260, 720

# setting up the main game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Angry Birds')

# colors
BLUE = (100, 100, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (50, 205, 50)

# creating borders
RIGHT_BORDER = pygame.Rect(WIDTH-10, 0, 10, HEIGHT)
FLOOR = pygame.Rect(0, HEIGHT-10, WIDTH, 10)
LEFT_BORDER = pygame.Rect(0, 0, 10, HEIGHT)

# loading fonts
VEL_FONT = pygame.font.SysFont('comicsans', 30)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
LEVEL_FONT = pygame.font.SysFont('comicsans', 60)
INTRO_FONT = pygame.font.SysFont('comicsans', 40)

# loading images
RED_BIRD = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'bird.png')), (40, 40))
PIG = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'pig.png')), (40, 40))
OBSTACLE_VERT = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'wall.png')), (25, 250))
OBSTACLE_HORIZONTAL = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'wall_horizontal.png')),
    (250, 25))


class Window:
    '''
    Class window takes no parameters
    Only has methods responsible for the game window
    '''
    def draw_indicator(self, bird):
        '''
        Functions draws the predicted path
        of the bird when launched
        takes bird object as param
        '''
        x = bird.x + 20
        y = bird.y + 20
        time = 0
        for _ in range(10):
            x += bird.vel_x
            y -= bird.vel_y - time
            time += 3/4
            pygame.draw.circle(WIN, WHITE, [x, y], 3)

    def draw_winner(self):
        '''
        Function that renders winner's text and closes the game
        '''
        draw_text = WINNER_FONT.render('YOU WON', 1, GREEN)
        WIN.fill(BLUE)
        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2,
                 HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()

    def draw_loser(self):
        '''
        Function that renders loser's text and closes the game
        '''
        draw_text = WINNER_FONT.render('YOU LOST', 1, RED)
        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2,
                 HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()

    def draw_window(self, bird, level, number_of_tries, time):
        '''
        Function draw_window draws the main game window
        :param: bird
        :type: object of RedBird class
        :param: level
        :type: object of Level class
        :param: number_of_tries
        :type: int
        '''
        WIN.fill(BLUE)
        pygame.draw.rect(WIN, BLACK, FLOOR)
        pygame.draw.rect(WIN, BLACK, RIGHT_BORDER)
        pygame.draw.rect(WIN, BLACK, LEFT_BORDER)

        current_level = LEVEL_FONT.render(
            "Level: " + str(level.level + 1), 1, WHITE)
        tries_left = VEL_FONT.render(
            "Tries left: " + str(number_of_tries), 1, WHITE)
        bird_velocity = VEL_FONT.render(
            "Velocity: " + str(bird.vel), 1, WHITE)
        bird_angle = VEL_FONT.render(
            "Angle: " + str(90 - int(math.degrees(bird.angle))), 1, WHITE)
        time_left = VEL_FONT.render(
            "Time left: " + str(round(3-time/10, 1)), 1, WHITE)

        WIN.blit(RED_BIRD, (bird.x, bird.y))

        for pig in level.pigs:
            WIN.blit(PIG, (pig.x, pig.y))
        for obstacle_vert in level.obstacles_vert:
            WIN.blit(OBSTACLE_VERT, (obstacle_vert.x, obstacle_vert.y))
        for obstacle_hor in level.obstacles_hor:
            WIN.blit(OBSTACLE_HORIZONTAL, (obstacle_hor.x, obstacle_hor.y))

        WIN.blit(bird_velocity, (10, 10))
        WIN.blit(bird_angle, (10, 40))
        WIN.blit(tries_left, (10, 70))
        WIN.blit(time_left, (10, 100))
        WIN.blit(current_level, (500, 10))
        if time == 0:
            self.draw_indicator(bird)
        pygame.display.update()
