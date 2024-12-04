import pygame
import sys
import random

from clases.jugador import Jugador
from clases.carta import Carta

from funciones.complementarias import *

from ui.interfaz_grafica import *


ancho = 160
alto = 230

ancho_boton_opcion = 250
alto_boton_opcion = 70
y = 450

borde_superior = 600 // 2

tupla_valores = ("1", "2", "3", "4", "5", "6", "7", "10", "11", "12")
tupla_palos = ("espada", "basto", "oro", "copa")

jerarquia = {
    ("1", "espada"): 14,
    ("1", "basto"): 13,
    ("7", "espada"): 12,
    ("7", "oro"): 11,
    ("3", None): 10,
    ("2", None): 9,
    ("1", "oro"): 8,
    ("1", "copa"): 8,
    ("12", None): 7,
    ("11", None): 6,
    ("10", None): 5,
    ("7", "basto"): 4,
    ("7", "copa"): 4,
    ("6", None): 3,
    ("5", None): 2,
    ("4", None): 1,
    }

def crear_mazo(palos: tuple, valores: tuple) -> list:
        '''
        Crea el mazo de las cartas, se junta cada valor con cada palo
        Devuelve un mazo creado y mezclado
        '''

        mazo = [Carta(valor, palo) for palo in palos for valor in valores]
        random.shuffle(mazo)

        return mazo
    
def valor_carta(carta: Carta) -> int:
    '''
    Recibe una carta
    Agrega valor a cada carta
    Devuelve el valor de la carta, si no se encuentra la carta en la jerarquia devuelve 0
    '''

    clave_especifica = (carta.valor, carta.palo)

    clave_general = (carta.valor, None)

    return jerarquia.get(clave_especifica, jerarquia.get(clave_general, 0))
        

def comparar_cartas(carta1: Carta, carta2: Carta) -> any:
    '''
    Recibe 2 diferentes cartas
    Compara los valores de las cartas ingresadas y verifica cual es mayor
    Devuelve la carta ganadora, en caso de que los valores de las cartas sean iguales no devuelve nada
    '''
    valor1 = valor_carta(carta1)
    valor2 = valor_carta(carta2)

    print(f"DEBUG: {carta1} tiene valor {valor1}, {carta2} tiene valor {valor2}")

    if valor1 > valor2:
        print(f"{carta1} gana la ronda.")
        return carta1  
    elif valor2 > valor1:
        print(f"{carta2} gana la ronda.")
        return carta2  
    else:
        print("Empate.")
        return None  
    
def mostrar_estado(jugador1: Jugador, jugador2: Jugador):
    '''
    Recibe 2 jugadores
    Muestra los puntos de cada jugador y muestra sus manos
    '''
    print(f"\nPuntos {jugador1.nombre}: {jugador1.puntos} | Puntos {jugador2.nombre}: {jugador2.puntos}")
    print("")
    print(f"{jugador1.nombre} mano: {jugador1.mostrar_mano()}")
    print(f"{jugador2.nombre} mano: {jugador2.mostrar_mano()}")


def cargar_imagen(ruta: str) -> pygame.image:
    '''
    Recibe una ruta
    Carga la imagen del objeto y ajusta su tamaño
    Devuelve el objeto con su imagen cargada y ajustada
    '''
    tamaño_imagen_ancho = 99
    tamaño_imagen_alto = 162 

    imagen = pygame.image.load(ruta)
    imagen = pygame.transform.scale(imagen, (tamaño_imagen_ancho, tamaño_imagen_alto))
    return imagen

def generar_rectangulo_boton(imagen: pygame.image, x: int) -> any:
    '''
    Recibe una imagen
    Genera un boton en funcion de la imagen recibida
    Devuelve el boton 
    '''
    
    boton = imagen.get_rect(center=(ancho // 2, alto//2))
    boton.center = (x, y)

    return boton


def cargar_imagen_carta(mano: list) -> pygame.image:
    tamaño_imagen_ancho = 99
    tamaño_imagen_alto = 162
    imagen = pygame.image.load(f"assets/cartas/{mano}.jpg")
    imagen = pygame.transform.scale(imagen, (tamaño_imagen_ancho, tamaño_imagen_alto))
    return imagen

def pantalla_inicio(pantalla: pygame.Surface) -> str:
    '''
    Muestra una pantalla donde el jugador ingresa su nombre
    Devuelve el nombre ingresado por el jugador
    '''
    clock = pygame.time.Clock()
    input_box = pygame.Rect(400, 300, 400, 50)
    font = pygame.font.Font(None, 48)
    color_inactivo = gris
    color_activo = blanco
    color = color_inactivo
    activo = False
    nombre = ""
    mensaje = font.render("Ingrese su nombre:", True, (0, 0, 0))
    continuar = False

    fondo_mesa = pygame.image.load("assets/fondo_mesa.jpg").convert()
    
    while continuar == False:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(evento.pos):
                    activo = True
                else:
                    activo = False
                color = (lambda activo: color_activo if activo else color_inactivo)(activo)

            if evento.type == pygame.KEYDOWN:
                if activo:
                    if evento.key == pygame.K_RETURN:
                        if nombre.strip():  
                            nombre = nombre[:1].upper() + nombre[1:]
                            continuar = True
                    elif evento.key == pygame.K_BACKSPACE:  
                        nombre = nombre[:-1]
                    else:  
                        nombre += evento.unicode

       
        pantalla.blit(fondo_mesa, [0, 0])
        pantalla.blit(mensaje, (400, 250))  
        txt_surface = font.render(nombre, True, (0, 0, 0))
        width = max(400, txt_surface.get_width() + 10)
        input_box.w = width
        pantalla.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(pantalla, color, input_box, 2) 

        pygame.display.flip()
        clock.tick(30)

    return nombre


def iniciar_pantalla_principal():
    '''
    inicializa el juego y maneja la pantalla de inicio.
    '''
    
    pygame.init()
    pantalla = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Truco UTN")
    
    nombre_jugador = pantalla_inicio(pantalla)
    print(f"Nombre del jugador ingresado: {nombre_jugador}")

    iniciar_juego(pantalla, nombre_jugador)


def iniciar_juego(pantalla: pygame.surface, nombre_jugador: str):
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load("assets/musica_fondo.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.5)

    corriendo = True

    mazo = crear_mazo(tupla_palos, tupla_valores)
    jugador1 = Jugador(nombre_jugador)
    jugador2 = Jugador("Bot")

    jugador1.recibir_cartas(mazo[0:3])  
    jugador2.recibir_cartas(mazo[3:6])  

    print(jugador1.mostrar_mano())
    print(jugador2.mostrar_mano())

    fondo_mesa = pygame.image.load("assets/fondo_mesa.jpg").convert()
    fondo_ganador = pygame.image.load("assets/ganador_fondo.jpg")
    cartas_jugador = [
        {"carta": jugador1.mano[i], 
         "imagen": cargar_imagen_carta(jugador1.mano[i]), 
         "rect": generar_rectangulo_boton(cargar_imagen_carta(jugador1.mano[i]), 350 + i * 300), 
         "velocidad": 0} for i in range(3)
    ]

    cartas_bot = jugador2.mano[:]
    carta_bot_actual = None

    carta_en_centro = None
    turno_jugador = True  
    ronda_actual = 0
    delay_inicio = None 

    boton_jugar_carta = pygame.Rect(250, 600, ancho_boton_opcion, alto_boton_opcion)
    boton_truco = pygame.Rect(520, 600, ancho_boton_opcion, alto_boton_opcion)
    boton_rendirse = pygame.Rect(800, 600, ancho_boton_opcion, alto_boton_opcion)

    jugar_carta = False
    puntos_a_ganar = 1

    respuesta_truco = ["si", "no"]
    truco_cantado = False
    texto_truco = "Cantar Truco"
    texto_ganador = fuente.render("", True, negro)

    datos_del_juego = {
        "Nombre": jugador1.nombre,
        "Partidas ganadas": 0,
        "Partidas perdidas": 0,
        "Partidas empatadas": 0
    }

    while corriendo:
        pantalla.blit(fondo_mesa, [0, 0])      

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                return
            if evento.type == pygame.MOUSEBUTTONDOWN and turno_jugador:
                if boton_jugar_carta.collidepoint(evento.pos):
                    jugar_carta = True

                if boton_truco.collidepoint(evento.pos):
                    respuesta_truco = random.choice(respuesta_truco)
                    if respuesta_truco == "si":
                        truco_cantado = True
                        puntos_a_ganar = 2
                        texto_truco = "Cantar retruco"
                    else:
                        jugador1.ganar_punto(1)
                        puntos_a_ganar = 1
                        truco_cantado = True

                if boton_rendirse.collidepoint(evento.pos): 
                    pygame.mixer.music.stop()
                    datos_del_juego["Partidas perdidas"] += 1
                    guardar_record("registro.csv", datos_del_juego)
                    return
                
                for carta in cartas_jugador:
                    if jugar_carta == True:
                        if carta["rect"].collidepoint(evento.pos): 
                            print(f"Jugador juega: {carta['carta']}")
                            carta_en_centro = carta
                            carta["velocidad"] = -5  
                            turno_jugador = False  
                            jugar_carta = False

        if carta_en_centro:
            carta_en_centro["rect"].y += carta_en_centro["velocidad"]
            if carta_en_centro["rect"].centery <= borde_superior:  
                carta_en_centro["rect"].centery = borde_superior
                carta_en_centro["rect"].centerx = 550
                carta_en_centro["velocidad"] = 0

                # Turno npc
                if not turno_jugador and not carta_bot_actual:
                    carta_bot_actual = cartas_bot.pop(0)  
                    print(f"Bot juega: {carta_bot_actual}")

        if carta_bot_actual:
            carta_bot_rect = cargar_imagen_carta(carta_bot_actual).get_rect(center=(650, borde_superior))
            carta_bot_rect.y += -5  
            if carta_bot_rect.centery <= borde_superior:
                carta_bot_rect.centery = borde_superior

                if delay_inicio is None:
                    delay_inicio = pygame.time.get_ticks()

        if delay_inicio and pygame.time.get_ticks() - delay_inicio > 1000:
            ganador = comparar_cartas(carta_en_centro["carta"], carta_bot_actual)
            if ganador == carta_en_centro["carta"]:
                texto_ganador_mano = fuente.render(f"{jugador1.nombre} gana la mano", True, negro)
                jugador1.ganar_punto(puntos_a_ganar)
            elif ganador == carta_bot_actual:
                texto_ganador_mano = fuente.render(f"La máquina gana la mano", True, negro)
                jugador2.ganar_punto(puntos_a_ganar)
            else:
                texto_ganador_mano = fuente.render("Es un empate", True, negro)

            pantalla.blit(texto_ganador_mano, (480, 300))
            pygame.display.flip()
            pygame.time.delay(1500)

            cartas_jugador.remove(carta_en_centro)
            carta_en_centro = None
            carta_bot_actual = None

            delay_inicio = None
            ronda_actual += 1
            turno_jugador = True

        
        dibujar_boton(pantalla, boton_jugar_carta, cambiar_color_boton(boton_jugar_carta, detectar_colision_mouse()), "Jugar carta")
        dibujar_boton(pantalla, boton_truco, cambiar_color_boton(boton_truco, detectar_colision_mouse()), texto_truco)
        dibujar_boton(pantalla, boton_rendirse, cambiar_color_boton(boton_rendirse, detectar_colision_mouse()), "Rendirse")

        
        for carta in cartas_jugador:
            pantalla.blit(carta["imagen"], carta["rect"].topleft)

        
        if carta_bot_actual:
            carta_bot_rect = cargar_imagen_carta(carta_bot_actual).get_rect(center=(750, borde_superior))
            pantalla.blit(cargar_imagen_carta(carta_bot_actual), carta_bot_rect.topleft)

        if carta_en_centro:
            pantalla.blit(carta_en_centro["imagen"], carta_en_centro["rect"].topleft)

        # Activa el mensaje de "Truco si/no"
        texto_retruco = fuente.render(f"Truco: {respuesta_truco}", True, negro)
        if truco_cantado == True:
            pantalla.blit(texto_retruco, (80, 88))
        
        texto_puntaje = fuente.render(f"Puntaje: {jugador1.puntos}", True, negro)
        pantalla.blit(texto_puntaje, (80, 20))

        # Verifica si la ronda actual es 3, si es asi, revisa los puntos de cada jugador. 
        if ronda_actual == 3:
            if jugador1.puntos > jugador2.puntos:
                texto_ganador = fuente.render(f"Gana {jugador1.nombre}", True, negro)
                datos_del_juego["Partidas ganadas"] += 1
            elif jugador2.puntos > jugador1.puntos:
                texto_ganador = fuente.render("Gana la máquina", True, negro)
                datos_del_juego["Partidas perdidas"] += 1
            else:
                texto_ganador = fuente.render("Empate", True, negro)
                datos_del_juego["Partidas empatadas"] += 1

            guardar_record("registro.csv", datos_del_juego)

            pantalla.blit(fondo_ganador, [0,0]) 
            pantalla.blit(texto_ganador, (480, 300))
            pygame.display.flip()
            pygame.time.delay(2500)

            while True:
             pantalla.blit(fondo_mesa, [0, 0]) 
             texto_pregunta = fuente.render("jugar otra ronda?", True, negro)
             pantalla.blit(texto_pregunta, (450, 180))

                
             boton_si = pygame.Rect(400, 300, 150, 50)
             boton_no = pygame.Rect(600, 300, 150, 50)
             dibujar_boton(pantalla, boton_si, (200, 255, 200), "Sí")
             dibujar_boton(pantalla, boton_no, (255, 200, 200), "No")

             pygame.display.flip()

             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     if boton_si.collidepoint(event.pos):
                        ronda_actual = 0
                        jugador1.puntos = 0
                        jugador2.puntos = 0
                        jugador1.mano.clear()
                        jugador2.mano.clear()

                        mazo = crear_mazo()
                        jugador1.recibir_cartas(mazo[0:3])
                        jugador2.recibir_cartas(mazo[3:6])

                        cartas_jugador = [
                            {
                            "carta": jugador1.mano[i],
                            "imagen": cargar_imagen_carta(jugador1.mano[i]),
                            "rect": generar_rectangulo_boton(cargar_imagen_carta(jugador1.mano[i]), 350 + i * 300),
                            "velocidad": 0,
                            }
                            for i in range(3)
                        ]
                        cartas_bot = jugador2.mano[:]
                        carta_en_centro = None
                        turno_jugador = True
                        pygame.mixer.music.stop()
                        return
                        
                     
                     if boton_no.collidepoint(event.pos):
                            pygame.mixer.music.stop()
                            pygame.quit()
                            sys.exit()

                 clock.tick(60)

        pygame.display.flip()
        clock.tick(60)