#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

width = 800
height = 388
rad = 120
scale = .9
horizDist = 12
vertDist = 10
vertRow2 = -10

## Draw
screen.fill(WHITE)


pygame.draw.ellipse(screen, BLUE, (horizDist,vertDist,width/3*scale,height*2/3*scale),THICKNESS)
pygame.draw.ellipse(screen, BLACK, (horizDist+width/3,vertDist,width/3*scale,height*2/3*scale),THICKNESS)
pygame.draw.ellipse(screen, RED, (horizDist+width*2/3,vertDist,width/3*scale,height*2/3*scale),THICKNESS)

pygame.draw.ellipse(screen, YELLOW, (horizDist+width/6,vertDist+vertRow2+height/3,width/3*scale,height*2/3*scale),THICKNESS)
pygame.draw.ellipse(screen, GREEN, (horizDist+width/2,vertDist+vertRow2+height/3,width/3*scale,height*2/3*scale),THICKNESS)



#################################
##  DRAW OLYPIC RINGS HERE
##
##  hint, lookup pygame.draw
##  specifically circle, ellipse,
##  and arc.  Also, the width
##  parameter
#################################


## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
