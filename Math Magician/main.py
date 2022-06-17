import random
from datetime import time

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
<<<<<<< HEAD
   
=======
    ''' def __init__(self):
        self.center = Point()
        self.center.y = SCREEN_HEIGHT/2
        self.center.x = SCREEN_WIDTH/2
        self.list = []
        #Highest number that appears per equation
        self.maxNum = 3
        #smallest number that appears in equation.
        self.min = 1
        '''
>>>>>>> d37a65340361c7a455a7cc97c90b05a01a083b76

    def __init__(self, first, second, x, y):
        self.center = Point()
        self.center.y = y
        self.center.x = x
<<<<<<< HEAD
        self.firstTerm = first
        self.secondTerm = second
        self.text = f"{self.firstTerm} x {self.secondTerm}"

    def set(self):
        self.firstTerm = random.randint(self.min, self.maxNum)
        self.secondTerm = random.randint(self.min, self.maxNum)
        self.text = f"{self.firstTerm} x {self.secondTerm}"
    def draw(self):
        arcade.draw_text(self.text, self.center.x, self.center.y, arcade.color.WHITE, DEFAULT_FONT_SIZE)



=======
        self.maxNum = max
        self.min = min
        # Create the equation to display and get the answer.
        self.multiplicand = random.randrange(self.min, self.maxNum + 1)
        self.multiplier = random.randrange(self.min, self.maxNum + 1)
        self.answer = self.multiplicand * self.multiplier
        self.display = f"{self.multiplicand} x {self.multiplier}"

    def draw(self):
        arcade.draw_text(self.display, self.center.x + 20, self.center.y, arcade.color.WHITE, DEFAULT_FONT_SIZE)


class EquationList():
    def __init__(self):
        self.center = Point()
        self.center.y = SCREEN_HEIGHT/1.42 # Moved equations up
        self.center.x = SCREEN_WIDTH/2.2 # Centered the equations a little more
        self.maxEquations = 10 # Set to 10 for now.
        self.offset = 5
        self.max = 3
        self.min = 1
        self.list = []

    def addEquation(self):
        if len(self.list) < self.maxEquations:
            newEquation = Equation(self.max, self.min, self.center.x, self.center.y - self.offset)
            self.offset += 30
            self.list.append(newEquation)

    def draw(self):
        arcade.draw_text("Equations", self.center.x, self.center.y + 30, arcade.color.WHITE, DEFAULT_FONT_SIZE)
        for x in self.list:
            x.draw()
    
    def checkAnswer(self, userInput):
        # Should check the users input against the equations answer. Currently untested.
        i = 0
        for i in self.list:
            if userInput == i.answer:
                i += 1
                # Add the next equation
                self.addEquation()
                return True
            elif userInput != i.answer:
                return False


>>>>>>> d37a65340361c7a455a7cc97c90b05a01a083b76

class Turns():
    def __init__(self):
        self.turn = True
        self.center = Point()
        self.center.y = SCREEN_HEIGHT - 100
        self.center.x = SCREEN_WIDTH/2.15 # Seems to center the timer more.
        self.time_since_last_turn = 0
        self.turn_length = 15
        self.timerText = 0
<<<<<<< HEAD
        self.trigger = False
=======

>>>>>>> d37a65340361c7a455a7cc97c90b05a01a083b76
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
<<<<<<< HEAD
                self.turn_length = 40
                

    def draw(self):
        self.timerText = f"{self.turn_length - self.time_since_last_turn:.1f}"
        arcade.draw_text(self.timerText, self.center.x, self.center.y + 20, arcade.color.WHITE, DEFAULT_FONT_SIZE)
=======
                self.turn_length = 15

    def draw(self):
        self.timerText = f"{self.turn_length - self.time_since_last_turn:1f}"
        arcade.draw_text(self.timerText, self.center.x, self.center.y - 30, arcade.color.WHITE, DEFAULT_FONT_SIZE) # Switched the timer to be below player/enemy
>>>>>>> d37a65340361c7a455a7cc97c90b05a01a083b76
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



class Input():
    def __init__(self):
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        inputmanager = arcade.gui.UIInputText(500, 200, 100, 100, "INPUT")
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="bottom",
            align_y=150,
            child=inputmanager)
        )

    def draw(self):
        arcade.draw_rectangle_filled(520, 300, 200, 50, arcade.color.WHITE)
        self.uimanager.draw()



class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture(BACKGROUND_IMAGE)
        self.player = Player()
        self.enemy = Enemy()
        self.menu = Menu()
        self.held_keys = set()
        self.turn = Turns()
<<<<<<< HEAD
        self.trigger = False
        self.equation = []



       
       
        
        #self.equations.addEquation()
        self.maxEquations = MAX_EQUATIONS_START
        self.offset = OFFSET_START
        self.max = MAX_TERM_START 
        self.min = MIN_TERM_START
        self.equation_setup()



        # Menu Button
=======
        self.pause = PauseView(arcade.View)
        self.input = Input()

        # Creating a UI MANAGER to handle the UI
>>>>>>> d37a65340361c7a455a7cc97c90b05a01a083b76
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        # Creating Button using UIFlatButton
        start_button = arcade.gui.UIFlatButton(text="Menu",
                                               width=200)

        # Assigning our on_buttonclick() function
        start_button.on_click = self.on_buttonclick

        # Adding button in our uimanager
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                align_y=50,
                child=start_button)
        )

<<<<<<< HEAD

        input_field = arcade.gui.UIInputText(200, 200, color=arcade.color.WHITE, text_color=arcade.color.WHITE, font_size=24, width=200, text='Enter Answer here')
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                align_y=250,
                child=input_field)
        )

     
        

        
        self.input_field = arcade.gui.UIInputText( 200, 200, color=arcade.color.DARK_BLUE_GRAY, font_size=24, width=200, text='Enter Answer here')




=======
    def on_buttonclick(self, event):
        print("Why wont the freaking pause menu show up")
        self.pause.on_draw()
>>>>>>> d37a65340361c7a455a7cc97c90b05a01a083b76

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player.draw()
        self.enemy.draw()
        self.menu.draw()
        self.turn.draw()
        self.equations.draw()
        self.input.draw()

        self.uimanager.draw()
<<<<<<< HEAD

     



        if self.turn.turn == True:
            for x in self.equation:
                x.draw()
       

   

    
=======
>>>>>>> d37a65340361c7a455a7cc97c90b05a01a083b76

    def update(self, delta_time):
        self.check_keys()
        # Call update_health here for testing/display purposes, will need to it move to appropriate function later.
        self.player.update_life()
        self.enemy.update_life()
        self.turn.on_update(delta_time)
<<<<<<< HEAD
        
        
=======
        #self.turn.change(10 + time.time())

>>>>>>> d37a65340361c7a455a7cc97c90b05a01a083b76
        #self.check_collisions()

    def equation_setup(self):
        self.offset = 0
        i = 0
        while i < self.maxEquations:
            self.offset += OFFSET_INCREMENT
            newEquation = Equation(random.randint(self.min, self.max), random.randint(self.min, self.max), SCREEN_WIDTH/2, (SCREEN_HEIGHT/2 + 100 - self.offset))
            self.equation.append(newEquation)
            i += 1
        
       

    def check_equation(self):
        if self.turn.trigger == False:
            self.equation.list = []
            self.equation_setup()
            self.turn.trigger = True

    def update_text(self):
        print(f"updating the label with input text '{self.input_field.text}'")
        self.label.text = self.input_field.text

    def check_keys(self):
        if arcade.key.LEFT in self.held_keys or arcade.key.A in self.held_keys: 
            self.equations.addEquation() # Will need to remove!

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
    def on_key_press(self, key, modifiers):
        self.held_keys.add(key)
    def on_key_release(self, key, modifiers):
        self.held_keys.remove(key)


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        self.clear()
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT - SCREEN_HEIGHT,
                                          color=arcade.color.ORANGE)

        arcade.draw_text("PAUSED", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to reset",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")


WINDOW = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
