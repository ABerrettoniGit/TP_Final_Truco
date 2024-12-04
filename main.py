import pygame
import sys
from ui.interfaz_grafica import menu_principal
from funciones.logica_juego import *


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Truco UTN")


while True:
    accion = menu_principal(screen)  
    if accion == "jugar":
        iniciar_pantalla_principal()  
    elif accion == "salir":
        pygame.quit()
        sys.exit()

 