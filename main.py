# File created 27Dec-21 by Nitlix (NitlixisStation) and is reserved after a private license.

import pygame
import random
import math
import sys
import json
import requests



# initialize it
pygame.init()

def rotate(surface, angle, pivot, offset):
  """Rotate the surface around the pivot point.

  Args:
      surface (pygame.Surface): The surface that is to be rotated.
      angle (float): Rotate by this angle.
      pivot (tuple, list, pygame.math.Vector2): The pivot point.
      offset (pygame.math.Vector2): This vector is added to the pivot.
  """
  rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
  rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
  # Add the offset vector to the center/pivot point to shift the rect.
  rect = rotated_image.get_rect(center=pivot+rotated_offset)
  return rotated_image, rect  # Return the rotated image and shifted rect.



# configurations
frames_per_second = 24
window_height = 600
window_width = 400

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# creating window
display = pygame.display.set_mode((window_width, window_height))


coin = pygame.image.load('site-main/apps/games/data/gf/coin.png')
#coin = pygame.transform.scale(coin, (16, 16))


# creating our frame regulator
clock = pygame.time.Clock()

# forever loop
while True:
  # frame clock ticking
  clock.tick(frames_per_second)
  display.blit(coin, (0,0))
  # frame Drawing

  
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()