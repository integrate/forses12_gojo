import random
import pygame
import model

pygame.init()
screen = pygame.display.set_mode([600, 650])
font = pygame.font.SysFont('alice', 25)



def draw():
    picture = font.render("нажмите Е чтобы скрыть надписи", True, [0, 255, 216], )
    picture1 = font.render( "на экране " + str(len(model.h))+" шариков", True, [0, 255, 216], )
    picture2 = font.render("нажмите DEL чтобы стереть все шарики ", True, [0, 255, 216], )
    picture3 = font.render("нажмите 1 чтобы шарики зависли/продолжили полет ", True, [0, 255, 216], )
    picture4 = font.render("нажмите 2 чтобы запустить особый режим ", True, [0, 255, 216], )
    for t in model.h:
        pygame.draw.circle(screen, t['color'], [t['x'], t['y']], t['p'])
    if model.inscription:
        screen.blit(picture, [10, 10])
        screen.blit(picture1,[10,30])
        screen.blit(picture2,[10,50])
        screen.blit(picture3,[10,70])
        screen.blit(picture4,[10,90])


    pygame.display.flip()

    screen.fill([0, 0, 0])
