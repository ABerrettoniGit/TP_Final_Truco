import pygame
import sys
from ui.interfaz_grafica import menu_principal
from funciones.logica_juego import *


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Truco UTN")

# Mostrar el menú principal
while True:
    accion = menu_principal(screen)  # Llama al menú principal y espera una acción
    if accion == "jugar":
        iniciar_pantalla_principal()  # Inicia el juego
    elif accion == "salir":
        pygame.quit()
        sys.exit()

 