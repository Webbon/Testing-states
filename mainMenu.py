import buttons
import pygame, sys
from pygame.locals import *

class MainMenu():
    
    def __init__(self, window):
        """Creates the main menu class
        
        Creates:
            Buttons
        """
        self.window = window
        
        #Set dimensions of button on screen
        self.dimension_button = (200, 50)
        
        #Keeps track of buttons on screen
        self.buttons_in_use = []
        
        #Create menu buttons
        self.newGame((640,100), 'red')
        self.loadGame((640,200), 'red')
        self.options((640,300), 'red')
        self.exit((640,400), 'red')
        
    
    def newGame(self, position, color):
        
        self.newGame_button = buttons.Button(self.window, position, self.dimension_button, color, writing='New Game')
        
        #Keeps track of button
        self.buttons_in_use.append(self.newGame_button)
        
    
    def loadGame(self, position, color):

        self.loadGame_button = buttons.Button(self.window, position, self.dimension_button, color, writing='Load Game')
        
        #Keeps track of button
        self.buttons_in_use.append(self.loadGame_button)
    
    def options(self, position, color):
        
        self.options_button = buttons.Button(self.window, position, self.dimension_button, color, writing='Options')
        
        #Keeps track of button
        self.buttons_in_use.append(self.options_button)
        
        def on_click():
            print('hey')
        
        self.options_button.on_click(on_click)
        
        self.options_button.pressed_function()
    
    def exit(self, position, color):
        
        self.exit_button = buttons.Button(self.window, position, self.dimension_button, color, writing='Exit')
        
        #Keeps track of button
        self.buttons_in_use.append(self.exit_button)
    
    def update_buttons(self, mouse_coordinates):
        for button in self.buttons_in_use:
            button.highlight_button(mouse_coordinates)
    
    def mouse_click(self, button_clicked):
        #Mouse presses
        LEFT = 1
        MIDDLE = 2
        RIGHT = 3
        
        #Check for left click
        if button_clicked == 1:
            
            #Check for highlighted button
            for button in self.buttons_in_use:
                if button.highlight == True:
                    button.pressed_function
        
        #Check for right click
        if button_clicked == 3:
            pass
        
        #Check for middle click
        if button_clicked == 2:
            pass