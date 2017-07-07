# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from colors import *

class Button():
    
    def __init__(self, window, position, dimensions, color, writing='', fontSize=32):
        """Makes a button
        
        parameters:
            window is the windowSurface
            position is a tuple of x, y of the center of the button
            dimensions is a tuple of dimensions of button
            color all caps 
            text is by default empty string
            fontSize is set to 32 by default
        """
        self.window = window
        self.position = position
        self.dimensions = dimensions
        self.color = color.upper()
        self.writing = writing
        self.fontSize = fontSize
        
        #Set up highlight
        self.highlight = False
                
        #create the text
        self.make_text(fontSize)
        
        #Create vertices of rectangle
        self.vertices_of_rectangle = self.create_vertices()
        self.rectangle_x = self.vertices_of_rectangle[0][0]
        self.rectangle_y = self.vertices_of_rectangle[0][1]
        
        #Draw the text's background rectangle onto the surface
        self.draw_rectangle(self.color)
        
        #blit the text to the screen
        self.blit_text('white')
    
    
    def create_vertices(self):
        """Returns vertices of the rectangle that will be drawn"""
        
        #Extra width to be added 
        extra_width = self.dimensions[0] - self.textRect.width
        
        #Rectangles x position
        rectangle_x_coordinate = self.textRect.left - extra_width/2
        
        #Extra height to be added
        extra_height = self.dimensions[1] - self.textRect.height
        
        #rectangles y position
        rectangle_y_coordinate = self.textRect.top - extra_height/2
        
        return (
            (rectangle_x_coordinate, rectangle_y_coordinate),
            (rectangle_x_coordinate, rectangle_y_coordinate + self.dimensions[1]),
            (rectangle_x_coordinate + self.dimensions[0], rectangle_y_coordinate + self.dimensions[1]),
            (rectangle_x_coordinate + self.dimensions[0], rectangle_y_coordinate)
            )
    
    def draw_rectangle(self, color):
        """Returns a rectangle with a specific color"""
        pygame.draw.rect(
            self.window, 
            color_dict[color.upper()], 
            (self.rectangle_x, 
            self.rectangle_y, 
            self.dimensions[0], 
            self.dimensions[1])
            )
    
    def make_text(self, fontSize):    
        """Makes text with specific font Size"""
        
        #Set up font
        self.Font = pygame.font.SysFont(None, fontSize)
        
        #Set up text
        self.text = self.Font.render(self.writing, True, color_dict['WHITE'])
        self.textRect = self.text.get_rect()
        self.textRect.centerx = self.position[0]
        self.textRect.centery = self.position[1]
    
    def blit_text(self, color):
        #Set color of text
        self.text = self.Font.render(self.writing, True, color_dict[color.upper()])
        
        #blit the text to the screen
        self.window.blit(self.text, self.textRect)
    
    
    def highlight_button(self, mouse_coordinates):
        """Highlights the button that the mouse is on
        """
        if self.over_button(mouse_coordinates) and not self.highlight:
           
            #Draws the hihglighted rectangle 
            self.draw_rectangle('green')
            
            #Redraws the highlighted text
            self.blit_text('black')
            
            #Button is now highlighted
            self.highlight = True
        
        elif not self.over_button(mouse_coordinates) and self.highlight:
            
            #Redraws the unhighlighted rectangle
            self.draw_rectangle(self.color)
            
            #Redraws the unhighlighted text
            self.blit_text('white')
            
            #button no longer highlighted
            self.highlight = False
    
    def over_button(self, mouse_coordinates):
        """Determines whether the mouse is within the boundaries of the button.
        
        tuple > bool
        """
        
        x = mouse_coordinates[0]
        y = mouse_coordinates[1]
        
        #Makes sure mouse is inbetween the width of the button
        if x >= self.vertices_of_rectangle[0][0] and x <= self.vertices_of_rectangle[2][0]:
            #Makes sure mouse is inbetween the height of the button
            if y >= self.vertices_of_rectangle[0][1] and y <= self.vertices_of_rectangle[1][1]:
                return True
    
    def on_click(self, pressed_function):
        self.pressed_function = pressed_function