#!/usr/bin/env python

from random import randrange

import math
import pygame
from pygame.locals import *


##Settings
FPS = 30

#Colors
YELLOW = 222,240,50
BLACK = 0,0,0
RED = 255,0,0
WHITE = 255,255,255
PURPLE = 170,0,255

## Game
def game(width, height):
    # init
    screen = pygame.display.set_mode((width, height))
    done = False


    scale = 30
    motor = 0
    x = 250
    y = 250
    center = (x, y)
    top = (x,y+math.sqrt(3)/2*scale)
    bottom = (x,y-math.sqrt(3)/2*scale)
    left = ((x-scale)*motor,y-math.sqrt(3)/2*scale)
    right = ((x+scale)*motor,y+math.sqrt(3)/2*scale)
    midleft = ((x-scale)*motor/2,y)
    midright = ((x+scale)*motor/2,y)

    toplist = [top, midright, midleft]
    leftlist = [midleft, left, bottom]
    rightlist = [midright, right, bottom]

    vvelocity = 0
    hvelocity = 0

    while not done:
        #input

        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
            elif event.type == KEYDOWN and event.key == K_w:
                vvelocity += 10
            elif event.type == KEYUP and event.key == K_w:
                vvelocity -= 10
            elif event.type == KEYDOWN and event.key == K_s:
                vvelocity -= 10
            elif event.type == KEYUP and event.key == K_s:
                vvelocity += 10
            elif event.type == KEYDOWN and event.key == K_d:
                hvelocity += 10
            elif event.type == KEYUP and event.key == K_d:
                hvelocity -= 10
            elif event.type == KEYDOWN and event.key == K_a:
                hvelocity -= 10
            elif event.type == KEYUP and event.key == K_a:
                hvelocity += 10



        motor += 0.1
        dir = math.cos(motor)

        y -= vvelocity
        x += hvelocity


        center = (x, y)
        top = (x,y-(math.sqrt(3)/2*scale))
        bottom = (x,y+(math.sqrt(3)/2*scale))
        left = (x-scale*dir,y+math.sqrt(3)/2*scale)
        right = (x+scale*dir,y+math.sqrt(3)/2*scale)
        midleft = (x-scale*dir/2,y)
        midright = (x+scale*dir/2,y)

        toplist = [top, midright, midleft]
        leftlist = [midleft, left, bottom]
        rightlist = [midright, bottom, right]


        screen.fill(BLACK)
        clock = pygame.time.Clock()

        clock.tick(FPS)

        pygame.draw.polygon(screen, YELLOW, toplist)
        pygame.draw.polygon(screen, YELLOW, leftlist)
        pygame.draw.polygon(screen, YELLOW, rightlist)
        pygame.display.flip()

#        pygame.draw.line(screen, YELLOW, top, midleft)
#        pygame.draw.line(screen, YELLOW, midright, midleft)
#        pygame.draw.line(screen, YELLOW, midright, midleft)



print "hi"
game(500,500)
