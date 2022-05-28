from flask import request
import pygame, sys
import requests
from pygame.locals import *

pygame.init()
frames_per_second = 5
#Create a displace surface object
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

mainLoop = True

clock = pygame.time.Clock()
cx,cy = 0,0
while mainLoop:
    clock.tick(frames_per_second)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

    x,y = pygame.mouse.get_pos()
    print("x:" + str(x))
    print("cx:" + str(cx))
    if x != cx or y != cy:
        cx = x
        cy = y
        print('sent {"x":' + str(cx) + ',"y":'+str(cy)+'}')
        requests.get('https://api.nitlix.pro/api/v1/remote-manager/add-action?id=x&action=mouse&data={"x":' + str(cx) + ',"y":'+str(cy)+'}')
    pygame.display.update()

pygame.quit()