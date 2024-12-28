import pygame
import random

#inicializar a pygame
pygame.init()

#crear la pantalla y asignarle tamaño
pantalla = pygame.display.set_mode((800,600))

#Titulo e Icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

#jugador, cargar imagen y asignar la posicion inicial del jugador, y el cambio de movimiento
img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio =0

#variables del enemigo
img_enemigo = pygame.image.load('enemigo.png')
enemigo_x = random.randint(0,736)
enemigo_y = random.randint(50,200)
enemigo_x_cambio =0.3
enemigo_y_cambio = 50

#variables de la bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio =0
bala_y_cambio = 1
bala_visible = False

#funcion para asignar posicion del jugador
def jugador(x,y):

    pantalla.blit(img_jugador,(x, y))

#funcion para asignar posicion del enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x, y))

#funcion disparar
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

#loop del juego
se_ejecuta = True
while se_ejecuta:

    pantalla.blit(fondo, (0,0))
    #pantalla.fill((205, 144, 228)) RGB de la pantalla de fondo

    #loop para obtener todos los eventos
    for evento in pygame.event.get():
        #evento para terminar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #eventos de pulsado de teclas
        if evento.type==pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                disparar_bala(jugador_x, bala_y)

        # eventos de levantamiento de teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #modificar ubicacion del jugador
    jugador_x += jugador_x_cambio

    #mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    #movimiento bala
    if bala_visible:
        disparar_bala(jugador_x, bala_y)
        bala_y -= bala_y_cambio

    # modificar ubicacion del enemigo
    enemigo_x += enemigo_x_cambio

    # mantener dentro de bordes al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.3
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.3
        enemigo_y += enemigo_y_cambio

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    #actualizar
    pygame.display.update()