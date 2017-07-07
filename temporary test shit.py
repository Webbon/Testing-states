import pygame

#Test shit

#FPS shit
FPS = 60
fpsClock = pygame.time.Clock()

# How many seconds the "game" is played.
playtime = 0.0

def fps_Shit():
    """
    Sets fps and play time as caption
    """
    global playtime
    # Do not go faster than this framerate.
    milliseconds = fpsClock.tick(FPS) 
    playtime += milliseconds / 1000.0
    
    #Set fps text
    fpsClock.tick(FPS)
    # Print framerate and playtime in titlebar.
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(fpsClock.get_fps(), playtime)
    pygame.display.set_caption(text)


def hey():
    print('hey')

x = hey