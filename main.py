import time

import pygame

import model
import view,control

while True:
    time.sleep(1/100)
    control.pain()
    model.play()
    view.draw()
