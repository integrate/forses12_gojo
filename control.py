import pygame
import model

timer=pygame.event.custom_type()


def pain():
    z=pygame.event.get()
    for c in z:
        if c.type==pygame.QUIT:
            exit()
        if c.type==pygame.KEYDOWN and c.key==pygame.K_SPACE:
            model.key()
        if c.type==pygame.KEYDOWN and c.key==pygame.K_e:
            model.inscription=not model.inscription
        if c.type==pygame.KEYDOWN and c.key==pygame.K_DELETE:
            model.h.clear()
        if c.type==pygame.KEYDOWN and c.key==pygame.K_1 and model.f==0:
            model.f=1
        elif c.type==pygame.KEYDOWN and c.key==pygame.K_1 and model.f==1:
            model.f=0
        if c.type==pygame.KEYDOWN and c.key==pygame.K_1 and model.f==2:
            model.slow=not model.slow
        if  c.type==pygame.KEYDOWN and c.key==pygame.K_2:
            pygame.time.set_timer(timer, 100)
            model.modo='slowdown'
        if c.type==timer:
            model.boom(6)





