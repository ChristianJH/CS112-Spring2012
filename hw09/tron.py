#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame.locals import *

height = 480
width = 640

screen_size = width,height
background = 0,0,0
white = 255,255,255
red = 255,0,0
blue = 0,0,255

pygame.init()
pygame.key.set_repeat(1,50)
screen = pygame.display.set_mode(screen_size)
   
def main():
    hpos1 = 0
    vpos1 = 24
    dirx1 = 1
    diry1 = 0
    dir1 = "RIGHT"
    crash1 = False
    
    hpos2 = 63
    vpos2 = 24
    dirx2 = -1
    diry2 = 0
    dir2 = "LEFT"
    crash2 = False
    
    history=[(0,24),(63,24)]
    
    screen.fill(background)
    
    pygame.draw.rect(screen,red,(10*hpos1,10*vpos1,width/64,height/48))
    pygame.draw.rect(screen,blue,(10*hpos2,10*vpos2,width/64,height/48)) 
    
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
            elif event.type == KEYDOWN and event.key == K_w and dir1 != "DOWN":
                diry1 = -1
                dirx1 = 0
                dir1 = "UP"
            elif event.type == KEYDOWN and event.key == K_a and dir1 != "RIGHT":
                diry1 = 0
                dirx1 = -1
                dir1 = "LEFT"
            elif event.type == KEYDOWN and event.key == K_s and dir1 != "UP":
                diry1 = 1
                dirx1 = 0
                dir1 = "DOWN"
            elif event.type == KEYDOWN and event.key == K_d and dir1 != "LEFT":
                diry1 = 0
                dirx1 = 1
                dir1 = "RIGHT"
#Player 2
                
            elif event.type == KEYDOWN and event.key == K_UP and dir2 != "DOWN":
                diry2 = -1
                dirx2 = 0
                dir2 = "UP"
            elif event.type == KEYDOWN and event.key == K_LEFT and dir2 != "RIGHT":
                diry2 = 0
                dirx2 = -1
                dir2 = "LEFT"
            elif event.type == KEYDOWN and event.key == K_DOWN and dir2 != "UP":
                diry2 = 1
                dirx2 = 0
                dir2 = "DOWN"
            elif event.type == KEYDOWN and event.key == K_RIGHT and dir2 != "LEFT":
                diry2 = 0
                dirx2 = 1
                dir2 = "RIGHT"
                
        pygame.draw.rect(screen,red,(10*hpos1,10*vpos1,width/64,height/48))
        pygame.draw.rect(screen,blue,(10*hpos2,10*vpos2,width/64,height/48)) 
                
    #Auto Movement
        hpos1 += dirx1
        vpos1 += diry1
        
        hpos2 += dirx2
        vpos2 += diry2


    #Crashing Into a line
        if (hpos2,vpos2) in history:
            crash2 = True
        if (hpos1,vpos1) in history:
            crash1 = True 

        if crash2 == True and crash1 == True: 
            done = True 
            print "You both suck."
        elif crash2 == True:
            done = True
            print "Player 1 Wins."
        elif crash1 == True:
            done = True
            print "Player 2 Wins"

        history.append((hpos1,vpos1))
        history.append((hpos2,vpos2))

    #Crashing Into the edge

        if hpos1 >= 64 or hpos1 <= -1 or vpos1 >= 48 or vpos1 <= -1:
            done = True
            print "Player 2 Wins."

        if hpos2 >= 64 or hpos2 <= -1 or vpos2 >= 48 or vpos2 <= -1:
            done = True
            print "Player 1 Wins."

        pygame.display.flip()


endgame = False
while not endgame:
    main()

    done = False
    while not done:
        event = pygame.event.poll()
        if event.type == KEYUP and event.key == K_SPACE:
            done = True
        elif event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            done = True
            endgame = True

print "Done"
