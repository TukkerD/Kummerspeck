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
        self.healthBarSize = 150
        self.lifeMax = 150
        self.life = 150

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width, self.texture.height, self.texture, self.angle, 255)
        arcade.draw_rectangle_filled(self.center.x, self.center.y + 200, self.healthBarSize, 15, arcade.color.RED)
        #Just to illustrate
        self.life -= 1
        arcade.draw_rectangle_filled(self.center.x, self.center.y + 200, ((self.life/self.lifeMax) * self.healthBarSize), 15, arcade.color.GREEN)
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

class Equation():
    def __init__(self):
        self.center = Point()
        self.center.y = SCREEN_HEIGHT/2
        self.center.x = SCREEN_WIDTH/2
        self.list = []
        #Highest number that appears per equation
        self.maxNum = 3
        #smallest number that appears in equation.
        self.min = 1
    def __init__(self, max, min, x, y):
        self.center = Point()
        self.center.y = y
        self.center.x = x
        self.maxNum = max
        self.min = min
    def draw(self):
        arcade.draw_text("Equations", self.center.x, self. center.y, arcade.color.WHITE, DEFAULT_FONT_SIZE)

class EquationList():
    def __init__(self):
        self.center = Point()
        self.center.y = SCREEN_HEIGHT/2
        self.center.x = SCREEN_WIDTH/2
        self.maxEquations = 3
        self.offset = 0
        self.max = 3
        self.min = 1
        self.list = []
    def addEquation(self):
        i = 0
        while i < self.maxEquations:
            self.offset += 30
            newEquation = Equation(self.max, self.min, (self.center.x - self.offset), self.center.y)
            self.list.append(newEquation)
    def draw(self):
        for x in self.list():
            x.draw()


class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture(BACKGROUND_IMAGE)
        self.player = Player()
        self.enemy = Enemy()
        self.held_keys = set()
        self.equations = EquationList()
        #self.equations.addEquation()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player.draw()
        self.enemy.draw()
        #self.equations.draw()

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
