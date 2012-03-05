#!/usr/bin/env python

from random import randrange

import pygame
from pygame.locals import *

## Settings

FPS = 30
pygame.font.init()



#Colors
C_BORDER = 0,0,0
C_HIDDEN = 251,248,239
C_ACTIVE = 94,143,201
C_CLEARED = 120,164,218
C_BOMB = 255,0,0
C_1 = 255,0,0
C_2 = 255,153,0
C_3 = 222,253,53
C_4 = 0,255,0
C_5 = 0,0,255
C_6 = 255,0,255
C_7 = 255,255,255
C_8 = 0,0,0
C_FLAGGED = C_2


def clear_square(world,x,y):
    if not world[x][y]["cleared"]:
        world[x][y]["cleared"] = True

def flag_square(world,x,y):
    if world[x][y]["flagged"]:
        world[x][y]["flagged"] = False
    elif not world[x][y]["flagged"]:
        world[x][y]["flagged"] = True

def bomb_at(world,x,y):
    width = len(world)
    height = len(world[0])
    if x < 0 or x >= width or y < 0 or y >= height:
        return False
    else:
        return world[x][y]["bomb"]

def draw_1(font, screen, rect):
    words = font.render("1", True, C_1)
    loc = words.get_rect()
    loc.center = rect.center
    screen.blit(words, loc)#X and Y are where you want the  words to appear.

def draw_2(font, screen, rect):
    words = font.render("2", True, C_2)
    loc = words.get_rect()
    loc.center = rect.center
    screen.blit(words, loc)#X and Y are where you want the  words to appear.

def draw_3(font, screen, rect):
    words = font.render("3", True, C_3)
    loc = words.get_rect()
    loc.center = rect.center
    screen.blit(words, loc)#X and Y are where you want the  words to appear.

def draw_4(font, screen, rect):
    words = font.render("4", True, C_4)
    loc = words.get_rect()
    loc.center = rect.center
    screen.blit(words, loc)#X and Y are where you want the  words to appear.

def draw_5(font, screen, rect):
    words = font.render("5", True, C_5)
    loc = words.get_rect()
    loc.center = rect.center
    screen.blit(words, loc)#X and Y are where you want the  words to appear.

def draw_6(font, screen, rect):
    words = font.render("6", True, C_6)
    loc = words.get_rect()
    loc.center = rect.center
    screen.blit(words, loc)#X and Y are where you want the  words to appear.

def draw_7(font, screen, rect):
    words = font.render("7", True, C_7)
    loc = words.get_rect()
    loc.center = rect.center
    screen.blit(words, loc)#X and Y are where you want the  words to appear.

def draw_8(font, screen, rect):
    words = font.render("8", True, C_8)
    loc = words.get_rect()
    loc.center = rect.center
    screen.blit(words, loc)#X and Y are where you want the  words to appear.



## Game
def game(tile, width, height, num_bombs):
    # init
    screen = pygame.display.set_mode((width*tile, height*tile))
    font = pygame.font.Font(None, 40)

    # store all the game data
    world = []
    for x in range(width):
        row = []
        for y in range(height):
            cell = {}
            cell["bomb"] = False
            cell["hint"] = int(0)
            cell["rect"] = pygame.Rect(x*tile, y*tile, tile, tile)
            cell["cleared"] = False
            cell["flagged"] = False
            row.append(cell)
        world.append(row)

        for x in range(width):
            for y in range(height):    
                cell["bomb"] = False     
    # place bombs
    c = 0
    while c < num_bombs:
        x = randrange(width)
        y = randrange(height)
        if not world[x][y]["bomb"]:
            world[x][y]["bomb"] = True
            c += 1

    # define numbers
    for x in range(width):
        for y in range(height):
            if not world[x][y]["bomb"]:

                if bomb_at(world, x+1, y):
                    world[x][y]["hint"] += 1
                
                if bomb_at(world, x+1, y+1):
                    world[x][y]["hint"] += 1

                if bomb_at(world, x+1, y-1):
                    world[x][y]["hint"] += 1

                if bomb_at(world, x-1, y):
                    world[x][y]["hint"] += 1

                if bomb_at(world, x-1, y+1):
                    world[x][y]["hint"] += 1

                if bomb_at(world, x-1, y-1):
                    world[x][y]["hint"] += 1

                if bomb_at(world, x, y+1):
                    world[x][y]["hint"] += 1

                if bomb_at(world, x, y-1):
                    world[x][y]["hint"] += 1

    ## flags
    lmb_clicked = False
    action_clear_square = False
    rmb_clicked = False
    action_flag_square = False

    # loop
    clock = pygame.time.Clock()
    done = False
    progress = width * height
    winAbility = True
    won = False
    while not done:
        # input
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True

            # mouse
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                lmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                lmb_clicked = False
                action_clear_square = True

            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                rmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                rmb_clicked = False
                action_flag_square = True

        # update
        if winAbility == True and won == False:
            if action_clear_square:
                x,y = pygame.mouse.get_pos()
                x /= tile
                y /= tile
                if not world[x][y]["flagged"]:
                    if not world[x][y]["cleared"]:
                        clear_square(world, x, y)
                        progress -= 1
                        print world[x][y]["hint"] 
                    else:
                        print world[x][y]["hint"]     
                if world[x][y]["bomb"]:
                    if not world[x][y]["flagged"]:
                        print "YOU SUCK."      
                        winAbility = False 
                        for x in range(width):
                            for y in range(height): 
                                if world[x][y]["bomb"]:
                                    print "BOOM!"
                action_clear_square = False
            

            if action_flag_square:
                x,y = pygame.mouse.get_pos()
                x /= tile
                y /= tile
                flag_square(world, x, y)
                action_flag_square = False
                print world[x][y]["hint"]

            if progress == num_bombs and winAbility == True:
                won = True


        # display
        screen.fill(C_BORDER)

        # draw each cell
        for x in range(width):
            for y in range(height):
                # get rect for cell
                rect = world[x][y]["rect"]

                # color for cell
                if world[x][y]["cleared"]:
                    bg_color = C_CLEARED
                elif lmb_clicked and rect.collidepoint(pygame.mouse.get_pos()):
                    bg_color = C_ACTIVE
                elif world[x][y]["flagged"]:
                    bg_color = C_FLAGGED
                else:
                    bg_color = C_HIDDEN

                # draw background
                screen.fill(bg_color, rect.inflate(-2, -2))

                # draw cleared graphics
                if world[x][y]["cleared"]:
                    if world[x][y]["hint"]==1:
                        draw_1(font, screen, rect)
                    if world[x][y]["hint"]==2:
                        draw_2(font, screen, rect)
                    if world[x][y]["hint"]==3:
                        draw_3(font, screen, rect)
                    if world[x][y]["hint"]==4:
                        draw_4(font, screen, rect)
                    if world[x][y]["hint"]==5:
                        draw_5(font, screen, rect)
                    if world[x][y]["hint"]==6:
                        draw_6(font, screen, rect)
                    if world[x][y]["hint"]==7:
                        draw_7(font, screen, rect)
                    if world[x][y]["hint"]==8:
                        draw_8(font, screen, rect) 
                    if world[x][y]["bomb"]:
                        pygame.draw.ellipse(screen, C_BOMB, rect.inflate(-tile/2, -tile/2))
                if winAbility == False:
                    if world[x][y]["bomb"]:
                        pygame.draw.ellipse(screen, C_BOMB, rect.inflate(-tile/2, -tile/2))
                        draw_2(font, screen, rect)
#                if won == True:
#                    for x in range(width):
#                        for y in range(height):
#                            if world[x][y]["bomb"]:
#                                bg_color = C_FLAGGED



        # refresh
        pygame.display.flip()
        clock.tick(FPS)


# Application
def main():
    pygame.init()
    game(50, 10, 10, 10)


main()
print "ByeBye"













