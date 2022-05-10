import os


import os
import sys

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

ROOT = os.path.dirname(sys.modules['__main__'].__file__)
BACKGROUND_IMAGE = ROOT + "/images/background.png" 
MINOTAUR = ROOT + "/images/minotaur.png" 
SLIME = ROOT + "/images/slime.png" 
WIZARD= ROOT + "/images/wizard.png" 

DEFAULT_FONT_SIZE = 20
OFFSET_INCREMENT = 30