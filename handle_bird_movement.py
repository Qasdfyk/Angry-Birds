import pygame
from window import HEIGHT, WIDTH

BIRD_DIED = pygame.USEREVENT + 1
ROUND_LOST = pygame.USEREVENT + 2
ROUND_WON = pygame.USEREVENT + 3


def border_collision(bird):
    '''
    Function that takes RedBird class object as param
    and handles its collision with borders
    '''
    if bird.x > WIDTH-bird.width-10:
        bird.x = WIDTH-bird.width-10
        bird.vel_x = -bird.vel_x

    if bird.y > HEIGHT-bird.height-10:
        bird.y = HEIGHT-bird.height-10
        bird.vel_y = -bird.vel_y*(95/100)
        bird.vel_x = (9/10)*bird.vel_x

    if bird.x <= 10:
        bird.x = 10
        bird.vel_x = -bird.vel_x


def pig_collisions(bird, level):
    '''
    Function that takes RedBird class object and current
    level which is Level class object as params
    and handles RedBirds collisions with pigs
    '''
    for pig in level.pigs:
        if bird.frame.colliderect(pig.frame) and level.pigs_left <= 1:
            level.pigs_left -= 1
            pig.kill()
            level.kill()
            pygame.event.post(pygame.event.Event(ROUND_WON))

        if bird.frame.colliderect(pig.frame):
            pig.kill()
            level.pigs_left -= 1


def obstacle_vert_collsion(bird, level):
    '''
    Function that takes RedBird class object and current
    level which is Level class object as params
    and handles RedBirds collisions with vertical obstacles
    '''
    for obstacle_vert in level.obstacles_vert:
        if bird.frame.colliderect(obstacle_vert.frame):
            if bird.vel_y < 0 and bird.y - bird.height <= obstacle_vert.y:
                bird.y = obstacle_vert.y - bird.height
                bird.vel_y = -bird.vel_y
            elif bird.vel_y > 0 and bird.y + bird.width >= obstacle_vert.y + obstacle_vert.height:
                bird.y = obstacle_vert.y + obstacle_vert.height
                bird.vel_y = -bird.vel_y
            else:
                if bird.vel_x > 0:
                    bird.vel_x = -bird.vel_x
                    bird.x = obstacle_vert.x - bird.width
                elif bird.vel_x <= 0:
                    bird.vel_x = -bird.vel_x
                    bird.x = obstacle_vert.x + obstacle_vert.width


def obstacle_hor_collsion(bird, level):
    '''
    Function that takes RedBird class object and current
    level which is Level class object as params
    and handles RedBirds collisions with horizontal obstacles
    '''
    for obstacle_hor in level.obstacles_hor:
        if bird.frame.colliderect(obstacle_hor.frame):
            if bird.vel_x > 0 and bird.x <= obstacle_hor.x:
                bird.x = obstacle_hor.x - bird.width
                bird.vel_x = -bird.vel_x
            elif bird.vel_x < 0 and bird.x - bird.width >= obstacle_hor.x + obstacle_hor.width:
                bird.x = obstacle_hor.x + obstacle_hor.width
                bird.vel_x = -bird.vel_x
            else:
                if bird.vel_y > 0:
                    bird.y = obstacle_hor.y + obstacle_hor.height
                    bird.vel_y = -bird.vel_y
                elif bird.vel_y <= 0:
                    bird.y = obstacle_hor.y - bird.height
                    bird.vel_y = -bird.vel_y


def bird_death_event(bird, time, tries_left):
    '''
    Function that takes RedBird class object, current time,
    tries_left and handles RedBirds deaths
    '''
    if time > 30 and tries_left == 1:
        pygame.event.post(pygame.event.Event(ROUND_LOST))
        bird.kill()

    if time > 30 and tries_left > 1:
        pygame.event.post(pygame.event.Event(BIRD_DIED))
        bird.reset()
