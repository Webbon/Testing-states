import pygame, sys
from pygame.locals import *
import buttons, mainMenu

import temporary


pygame.init()

windowSize = (1280, 600) #(1280, 720) Replace later
center_x_window, center_y_window = windowSize[0]/2, windowSize[1]/2 
windowSurface = pygame.display.set_mode(windowSize, 0, 32)
#pygame.FULLSCREEN Replace later

main_menu = mainMenu.MainMenu(windowSurface)

#Mouse presses
LEFT = 1
MIDDLE = 2
RIGHT = 3

#Set up game states, such as main menu, gameplay
game_state = [main_menu]

#Run the game loop
while True:
    
    for event in pygame.event.get():
        #Check if window is closed
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
        
        #Check for button presses
        if event.type == KEYDOWN:
            
            #Pause game
            if event.key == K_ESCAPE:
                pygame.display.quit()
                sys.exit()
            
            #TEST REMOVE LATER
            if event.key == K_SPACE:
                print(pygame.mouse.get_pos())
        
        #Check for mouse presses
        if event.type == MOUSEBUTTONDOWN:
            #Function of the mouse press
            game_state[-1].mouse_click(event.button)
        
    #Checks for buttons
    game_state[-1].update_buttons(pygame.mouse.get_pos())
            
            
    #TEST REMOVE LATER
    temporary.fps_Shit()
    
    #Draw the window onto the screen
    pygame.display.update()

pygame.quit()