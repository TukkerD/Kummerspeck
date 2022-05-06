import random
import arcade
from constants import *

HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25


class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


class Player():
    def __init__(self):
        super().__init__()

        self.center = Point()
        self.center.y = SCREEN_HEIGHT / 2
        self.center.x = SCREEN_WIDTH - 100
        self.angle = 0
        self.image = WIZARD
        self.texture = arcade.load_texture(self.image, flipped_horizontally=True)

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width, self.texture.height, self.texture, self.angle, 255)

    def advance(self):
        self.center.y += 0
        self.center.x += 0


class Enemy():
    def __init__(self):
        super().__init__()
        self.center = Point()
        self.center.y = SCREEN_HEIGHT/2
        self.center.x = SCREEN_WIDTH/8
        self.angle = 0
        self.image = MINOTAUR
        self.texture = arcade.load_texture(self.image, flipped_horizontally=True)

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width, self.texture.height, self.texture, self.angle, 255)
       
    def advance(self):
        self.center.y += 0
        self.center.x += 0


class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture(BACKGROUND_IMAGE)
        self.player = Player()
        self.enemy = Enemy()
        self.held_keys = set()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player.draw()
        self.enemy.draw()

    def update(self, delta_time):
        self.check_keys()
        #self.check_collisions()

    def check_keys(self):
        if arcade.key.LEFT in self.held_keys or arcade.key.A in self.held_keys:
            print("left")

        if arcade.key.RIGHT in self.held_keys or arcade.key.D in self.held_keys:
            print("left")

        if arcade.key.UP in self.held_keys or arcade.key.W in self.held_keys:
            print("left")

        if arcade.key.DOWN in self.held_keys or arcade.key.S in self.held_keys:
            print("left")


WINDOW = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
