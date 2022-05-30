import random
import arcade
import schedule
from sympy import false, true
from constants import *
import arcade.gui
import threading

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
        self.center.x = SCREEN_WIDTH/8
        self.angle = 0
        self.image = WIZARD
        self.texture = arcade.load_texture(self.image)
        self.healthBarStart = SCREEN_WIDTH/8
        self.lifeMax = 150
        self.life = 150
        self.damage = 10
        # Change the rate that health is lost
        self.lifeRateChange = 0
       

    def draw(self):
        # Wizard
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width, self.texture.height, self.texture, self.angle, 255)
        # Health bars
        arcade.draw_rectangle_filled(self.center.x, self.center.y + 200, self.lifeMax, 15, arcade.color.RED)
        arcade.draw_rectangle_filled(self.healthBarStart, self.center.y + 200, self.life, 15, arcade.color.GREEN)
    def attack(self):
        return self.damage
    def hurt(self, incomingDamage):
        timeEnd = time.time() + .25

        while time.time() < timeEnd:
            self.lifeRateChange = incomingDamage
        self.lifeRateChange = 0


    def advance(self):
        self.center.y += 0
        self.center.x += 0

    def update_life(self):
        # Stop the health bar at 0 to avoid it going into the negative integers.
        if self.life <= 0:
            self.life = 0
            self.lifeRateChange = 0
        elif self.life > 0:
            
            # += to drain right to left, -= to drain left to right
            self.healthBarStart += (self.lifeRateChange / 2)
            self.life += self.lifeRateChange


class Enemy():
    def __init__(self):
        super().__init__()
        self.center = Point()
        self.center.y = SCREEN_HEIGHT/2
        self.center.x = SCREEN_WIDTH - 200
        self.angle = 0
        self.image = MINOTAUR
        self.texture = arcade.load_texture(self.image)
        self.healthBarStart = SCREEN_WIDTH - 200
        self.lifeMax = 150
        self.life = 150
        self.damage = 5
        # Change the rate that health is lost
        

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width, self.texture.height, self.texture, self.angle, 255)
        #Health Bars
        arcade.draw_rectangle_filled(self.center.x, self.center.y + 200, self.lifeMax, 15, arcade.color.RED)
        arcade.draw_rectangle_filled(self.healthBarStart, self.center.y + 200, self.life, 15, arcade.color.GREEN)

    def advance(self):
        self.center.y += 0
        self.center.x += 0

    def attack(self):
        return self.damage
    def hurt(self, incomingDamage):
        timeEnd = time.time() + .25

        while time.time() < timeEnd:
            self.lifeRateChange = incomingDamage
        self.lifeRateChange = 0

    def update_life(self):
        # Stop the health bar at 0 to avoid it going into the negative integers.
        if self.life <= 0:
            self.life = 0
            self.lifeRateChange = 0
        #elif self.life > 0:
            # += to drain right to left, -= to drain left to right
            self.healthBarStart += (self.lifeRateChange / 2)
            self.life += self.lifeRateChange
            


class Equation():
   

    def __init__(self, max, min, x, y):
        self.center = Point()
        self.center.y = y
        self.center.x = x
        self.maxNum = max
        self.min = min
        self.firstTerm = 0
        self.secondTerm = 0
        self.text = f"{self.firstTerm} x {self.secondTerm}"

    def set(self):
        self.firstTerm = random.randint(self.min, self.maxNum)
        self.secondTerm = random.randint(self.min, self.maxNum)
        self.text = f"{self.firstTerm} x {self.secondTerm}"
    def draw(self):
        arcade.draw_text(self.text, self.center.x, self.center.y, arcade.color.WHITE, DEFAULT_FONT_SIZE)




class Turns():
    def __init__(self):
        self.turn = True
        self.center = Point()
        self.center.y = SCREEN_HEIGHT - 100
        self.center.x = SCREEN_WIDTH/2
        self.time_since_last_turn = 0
        self.turn_length = 15
        self.timerText = 0
        self.trigger = False
    def on_update(self, delta_time: float = 1 / 60):
        self.time_since_last_turn += delta_time
        
        if self.time_since_last_turn >= self.turn_length:
            if self.turn == True:
                self.turn = False
                self.time_since_last_turn = 0
                self.turn_length = 10
                self.trigger = False
            else:
                self.turn = True
                self.time_since_last_turn = 0
                self.turn_length = 40
                

    def draw(self):
        self.timerText = f"{self.turn_length - self.time_since_last_turn:1f}"
        arcade.draw_text(self.timerText, self.center.x, self.center.y + 20, arcade.color.WHITE, DEFAULT_FONT_SIZE)
        if self.turn == True:
            arcade.draw_text("Player", self.center.x, self.center.y, arcade.color.WHITE, DEFAULT_FONT_SIZE)  
        else:
            arcade.draw_text("Enemy", self.center.x, self.center.y, arcade.color.WHITE, DEFAULT_FONT_SIZE)
 
           

        
class Menu():
    def __init__(self):
        self.center = Point()
        self.center.y = 125
        self.center.x = SCREEN_WIDTH/2

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, SCREEN_WIDTH, 250, arcade.color.BLACK)
        #arcade.draw_text("menu", self.center.x, self.center.y, arcade.color.WHITE, DEFAULT_FONT_SIZE)


class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture(BACKGROUND_IMAGE)
        self.player = Player()
        self.enemy = Enemy()
        self.menu = Menu()
        self.held_keys = set()
        self.turn = Turns()
        self.trigger = False
        self.equation = []



       
       
        
        #self.equations.addEquation()
        self.maxEquations = 3
        self.offset = 0
        self.max = 3
        self.min = 1
        self.equation_setup()

        # Menu Button
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        start_button = arcade.gui.UIFlatButton(text="Menu",
                                               width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                align_y=150,
                child=start_button)
        )


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player.draw()
        self.enemy.draw()
        self.menu.draw()
        self.turn.draw()
        # Render button
        self.uimanager.draw()

        

        for x in self.equation:
            x.draw()
       

   

    

    def update(self, delta_time):
        self.check_keys()
        # Call update_health here for testing/display purposes, will need to it move to appropriate function later.
        self.player.update_life()
        self.enemy.update_life()
        self.turn.on_update(delta_time)
        
        
        #self.check_collisions()

    def equation_setup(self):
        self.offset = 0
        i = 0
        while i < self.maxEquations:
            self.offset += 30
            newEquation = Equation(self.max, self.min, SCREEN_WIDTH/2, (SCREEN_HEIGHT/2 - self.offset))
            self.equation.append(newEquation)
            i += 1

       

    def check_equation(self):
        if self.turn.trigger == False:
            self.equation.list = []
            self.equation_setup()
            self.turn.trigger = True

    def check_keys(self):
        if arcade.key.LEFT in self.held_keys or arcade.key.A in self.held_keys:
            print("left")

        if arcade.key.RIGHT in self.held_keys or arcade.key.D in self.held_keys:
            print("left")

        if arcade.key.UP in self.held_keys or arcade.key.W in self.held_keys:
            print("left")

        if arcade.key.DOWN in self.held_keys or arcade.key.S in self.held_keys:
            print("left")

    '''
    Added the key press functions for testing functions outside of the update function
    just remove the comment tags and place your function in check_keys
    '''
    #def on_key_press(self, key, modifiers):
        #self.held_keys.add(key)
    #def on_key_release(self, key, modifiers):
        #self.held_keys.remove(key)

  



WINDOW = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
