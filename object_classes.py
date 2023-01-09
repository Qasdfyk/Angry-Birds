import pygame
from math import pi, sin, cos
from handle_bird_movement import (
    border_collision, pig_collisions,
    obstacle_hor_collsion, obstacle_vert_collsion,
    bird_death_event,
)


class RedBird:
    '''
    Class Redbird
    takes no params
    when created has pre set parameters:
    x - x coordinate
    y - y coordinate
    height, width - size of the self
    vel, angle - velocity and angle of the self when created
    health
    vel_x, vel_y - velocity components based on the angle
    all of the above type: int
    frame - pygame rectangle object which represents the shape of the self
    '''
    def __init__(self):
        self.x = 50
        self.y = 670
        self.height = 40
        self.width = 40

        self.angle = pi/4
        self.vel = 25

        self.vel_x = self.vel*sin(self.angle)
        self.vel_y = self.vel*cos(self.angle)

    def reset(self):
        '''
        Resets the bird, sets the initial parameters
        '''
        self.x = 50
        self.y = 670
        self.angle = pi/4
        self.vel = 25
        self.health = 5
        self.vel_x = self.vel*sin(self.angle)
        self.vel_y = self.vel*cos(self.angle)

    def kill(self):
        self.x = 10000
        self.y = 0
        self.vel_x = 0
        self.vel_y = 0

    def movement(self, level, time, tries_left):
        '''
        Function responsible for calculating the position of the bird
        while the bird is moving
        '''
        self.frame = pygame.Rect(self.x, self.y, 40, 40)
        self.vel_y -= round(1/5*time, 5)
        self.x += self.vel_x
        self.y -= self.vel_y

        border_collision(self)
        pig_collisions(self, level)
        obstacle_vert_collsion(self, level)
        obstacle_hor_collsion(self, level)
        bird_death_event(self, time, tries_left)

    def set_params(self, event):
        '''
        Function that lets the player set parameters of the
        launch using keyboard
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.angle > pi/64:
                self.angle -= pi/50
            if event.key == pygame.K_DOWN and self.angle < 31*pi/64:
                self.angle += pi/50
            if event.key == pygame.K_LEFT and self.vel > 1:
                self.vel -= 1
            if event.key == pygame.K_RIGHT and self.vel < 45:
                self.vel += 1
        self.vel_x = self.vel*sin(self.angle)
        self.vel_y = self.vel*cos(self.angle)


class Pig:
    '''
    Class Pig
    takes x, y params which are coordinates :type: int
    has pre set params: height, lenght :type: int
    frame - pygame rectangle object which represents the shape of the pig
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 40
        self.width = 40
        self.frame = pygame.Rect(self.x, self.y, 40, 40)

    def kill(self):
        self.x = 10000
        self.y = 0
        self.vel_x = 0
        self.vel_y = 0
        self.frame = pygame.Rect(10000, 1000, 0, 0)


class ObstacleVertical:
    '''
    Class ObjectVertical
    takes x, y params which are coordinates :type: int
    has pre set params: height, lenght :type: int
    frame - pygame rectangle object which represents the shape of the object
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 250
        self.width = 25
        self.frame = pygame.Rect(self.x,
                                 self.y,
                                 self.width,
                                 self.height)

    def kill(self):
        self.x = 10000
        self.y = 0
        self.vel_x = 0
        self.vel_y = 0
        self.frame = pygame.Rect(10000, 1000, 0, 0)


class ObstacleHorizonal():
    '''
    Class ObjectHorizontal
    takes x, y params which are coordinates :type: int
    has pre set params: height, lenght :type: int
    frame - pygame rectangle object which represents the shape of the object
    '''
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.height = 25
        self.width = 250
        self.frame = pygame.Rect(self.x,
                                 self.y,
                                 self.width,
                                 self.height)

    def kill(self):
        self.x = 10000
        self.y = 0
        self.vel_x = 0
        self.vel_y = 0
        self.frame = pygame.Rect(10000, 1000, 0, 0)


class Level():
    '''
    Class Level as parameters takes lists of objects
    -pigs :type: list of objects of class Pig
    -obstacles_vert :type: list of objects of class ObstacleVertcal
    -obstacles_hor :type: list of objects of class ObstacleHorizontal
    -pigs_left how many pigs are left in the level :type: int
    -level numer of level :type: int
    '''
    def __init__(self, pigs, obstacles_vert=None,
                 obstacles_hor=None, level=None):

        self.pigs = pigs
        self.obstacles_vert = obstacles_vert
        self.obstacles_hor = obstacles_hor
        self.pigs_left = len(pigs)
        self.level = level

    def kill(self):
        for obstacle_hor in self.obstacles_hor:
            obstacle_hor.kill()
        for obstacle_vert in self.obstacles_vert:
            obstacle_vert.kill()
