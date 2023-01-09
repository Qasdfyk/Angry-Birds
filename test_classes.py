from game_class import Game
from object_classes import (
    RedBird,
    Pig,
    ObstacleVertical,
    ObstacleHorizonal,
    Level
)
from window import Window
import pygame


def test_create_bird():
    bird = RedBird()
    assert bird.x == 50
    assert bird.y == 670
    assert bird.height == 40
    assert bird.width == 40


def test_bird_kill():
    bird = RedBird()
    assert bird.x == 50
    assert bird.y == 670
    bird.kill()
    assert bird.x == 10000
    assert bird.y == 0


def test_pig_create():
    pig = Pig(50, 670)
    assert pig.x == 50
    assert pig.y == 670
    assert pig.height == 40
    assert pig.width == 40


def test_pig_kill():
    pig = Pig(50, 670)
    assert pig.x == 50
    assert pig.y == 670
    pig.kill()
    assert pig.x == 10000
    assert pig.y == 0


def test_obstcle_vert_create():
    obs_vert = ObstacleVertical(100, 100)
    assert obs_vert.x == 100
    assert obs_vert.y == 100
    assert obs_vert.height == 250
    assert obs_vert.width == 25


def test_obstacle_vert_kill():
    obs_vert = ObstacleVertical(100, 100)
    assert obs_vert.x == 100
    assert obs_vert.y == 100
    obs_vert.kill()
    assert obs_vert.x == 10000
    assert obs_vert.y == 0


def test_obstcle_hor_create():
    obs_hor = ObstacleHorizonal(100, 100)
    assert obs_hor.x == 100
    assert obs_hor.y == 100
    assert obs_hor.height == 25
    assert obs_hor.width == 250


def test_obstacle_hor_kill():
    obs_hor = ObstacleHorizonal(100, 100)
    assert obs_hor.x == 100
    assert obs_hor.y == 100
    obs_hor.kill()
    assert obs_hor.x == 10000
    assert obs_hor.y == 0


def test_level_class():
    pig = Pig(100, 100)
    obs_vert = ObstacleVertical(100, 100)
    obs_hor = ObstacleHorizonal(100, 100)
    level = Level([pig], [obs_vert], [obs_hor], 1)
    assert level.pigs == [pig]
    assert level.obstacles_vert == [obs_vert]
    assert level.obstacles_hor == [obs_hor]
    assert level.level == 1


def test_game():
    game = Game()
    assert isinstance(game.bird, RedBird) is True
    assert isinstance(game.window, Window) is True
    assert game.game_stage == 0
    assert game.set_params == 1
    assert game.number_of_tries == 3
    assert game.run is True
