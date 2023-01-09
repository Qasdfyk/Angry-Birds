from handle_bird_movement import border_collision
from object_classes import (
    RedBird, Pig,
    ObstacleHorizonal, ObstacleVertical,
    Level
)


def test_border_collisions():
    bird = RedBird()
    bird.x = 1220
    assert bird.x == 1220
    assert bird.vel_x > 0
    border_collision(bird)
    assert bird.x == 1210
    assert bird.vel_x < 0


def test_pig_collisions():
    bird = RedBird()
    pig = Pig(100, 100)
    obs_vert = ObstacleVertical(100, 100)
    obs_hor = ObstacleHorizonal(100, 100)
    level = Level([pig], [obs_vert], [obs_hor], 1)
    bird.x = 100
    bird.y = 100
    bird.movement(level, 3, 100)
    assert pig.x == 10000
    assert pig.y == 0


def test_obstacle_collsion_vert():
    bird = RedBird()
    pig = Pig(100, 100)
    obs_vert = ObstacleVertical(200, 200)
    obs_hor = ObstacleHorizonal(600, 600)
    level = Level([pig], [obs_vert], [obs_hor], 1)
    bird.x = 200
    bird.y = 200
    assert bird.vel_x > 0
    assert bird.vel_y > 0
    bird.movement(level, 3, 100)
    assert bird.vel_x < 0
    assert bird.vel_y > 0


def test_obstacle_collsion_hor():
    bird = RedBird()
    pig = Pig(100, 100)
    obs_vert = ObstacleVertical(200, 200)
    obs_hor = ObstacleHorizonal(600, 600)
    level = Level([pig], [obs_vert], [obs_hor], 1)
    bird.x = 600
    bird.y = 600
    assert bird.vel_x > 0
    assert bird.vel_y > 0
    bird.movement(level, 3, 100)
    assert bird.vel_x > 0
    assert bird.vel_y < 0
