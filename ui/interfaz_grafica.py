import pygame
from clases.jugador import *

pygame.init()

blanco = (255, 255, 255)
azul = (0, 0, 255)
gris = (100, 100, 100)
gris_claro = (205, 205, 205)
negro = (0, 0, 0)

fuente = pygame.font.Font(None, 48)

def dibujar_boton(superficie: any, rect: any, color: pygame.color, texto: str):
    '''
    Recibe una superficie, rectangulo, color y texto
    Dibuja un boton con texto
    '''
    pygame.draw.rect(superficie, color, rect)
    text_surface = fuente.render(texto, True, negro)
    text_rect = text_surface.get_rect(center=rect.center)
    superficie.blit(text_surface, text_rect)

def detectar_colision_mouse() -> pygame.mouse:
    """
    Calcula la posicion del mouse dentro de la pantalla
    Devuelve la posicion del mouse
    """
    mouse_pos = pygame.mouse.get_pos()

    return mouse_pos

def cambiar_color_boton(boton, mouse_pos) -> pygame.color:
    '''
    Recibe un boton y la posicion del mouse
    Verifica si la posicion del mouse se encuentra sobre el boton, si este esta sobre el boton devuelve un color sino devuelve otro
    Devuelve un color
    '''
    if boton.collidepoint(mouse_pos):
        color = gris
    else:
        color = gris_claro
    
    return color

def menu_principal(pantalla) -> str:
    '''
    Recibe una pantalla
    Dibuja la pantalla principal(menu), maneja eventos, dibuja los botones y verifica que boton es clickeado
    Devuelve un str
    '''
    fondo_pantalla_inicio = pygame.image.load("assets/fondo_pantalla_inicio.jpg").convert()
    boton_jugar = pygame.Rect(570, 300, 150, 70)
    boton_salir = pygame.Rect(570, 400, 150, 70)

    corriendo = True
    while corriendo:
        pantalla.blit(fondo_pantalla_inicio, [0, 0])

        dibujar_boton(pantalla, boton_jugar, cambiar_color_boton(boton_jugar, detectar_colision_mouse()), "Jugar")
        dibujar_boton(pantalla, boton_salir, cambiar_color_boton(boton_salir, detectar_colision_mouse()), "Salir")

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):  
                    return "jugar"  
                if boton_salir.collidepoint(evento.pos):
                    return "salir" 

        pygame.display.flip()