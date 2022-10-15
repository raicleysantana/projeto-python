import pygame, sys, math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Exemplo com curva")
pi = 3.141592653
 
# sets the properties of the arc
color = (102, 255, 255)

start_angle = 0
stop_angle = math.pi
width = 10

while True: # main loop
    for event in pygame.event.get():
        # draws the arc
        pygame.draw.arc(screen, color, screen.get_rect(), start_angle, stop_angle, width)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()