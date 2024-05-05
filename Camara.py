import pygame
from pygame.locals import *

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No se ha detectado ningún joystick.")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print("Nombre del joystick:", joystick.get_name())
    print("Número de botones:", joystick.get_numbuttons())

    while True:
        for event in pygame.event.get():
            if event.type == JOYBUTTONDOWN:
                print("Botón {} presionado".format(event.button))

     








