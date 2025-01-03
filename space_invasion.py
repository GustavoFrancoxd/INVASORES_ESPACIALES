import pygame
import random
import math
from pygame import mixer

# Inicializar pygame
pygame.init()

# Crear la pantalla y asignarle tamaño
pantalla = pygame.display.set_mode((800, 600))

# Título e Icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# Agregar música
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

class Jugador:
    def __init__(self, x, y):
        self.img = pygame.image.load('cohete.png')
        self.x = x
        self.y = y
        self.x_cambio = 0

    def mover(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_cambio = -0.5
        elif keys[pygame.K_RIGHT]:
            self.x_cambio = 0.5
        else:
            self.x_cambio = 0

        self.x += self.x_cambio

        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

    def dibujar(self):
        pantalla.blit(self.img, (self.x, self.y))


class Enemigo:
    def __init__(self, x, y):
        self.img = pygame.image.load('enemigo.png')
        self.x = x
        self.y = y
        self.x_cambio = 0.5
        self.y_cambio = 50

    def mover(self):
        self.x += self.x_cambio

        if self.x <= 0:
            self.x_cambio = 0.5
            self.y += self.y_cambio
        elif self.x >= 736:
            self.x_cambio = -0.5
            self.y += self.y_cambio

    def dibujar(self):
        pantalla.blit(self.img, (self.x, self.y))


class Bala:
    def __init__(self, x, y):
        self.img = pygame.image.load('bala.png')
        self.x = x
        self.y = y
        self.velocidad = -3

    def mover(self):
        self.y += self.velocidad

    def dibujar(self):
        pantalla.blit(self.img, (self.x + 16, self.y + 10))


class Juego:
    def __init__(self):
        self.jugador = Jugador(368, 526)
        self.enemigos = [Enemigo(random.randint(0, 736), random.randint(50, 200)) for _ in range(8)]
        self.balas = []
        self.puntaje = 0
        self.fuente = pygame.font.Font('freesansbold.ttf', 32)
        self.texto_x = 10
        self.texto_y = 10
        self.fuente_final = pygame.font.Font('freesansbold.ttf', 40)

    def mostrar_puntaje(self):
        texto = self.fuente.render(f'Puntaje: {self.puntaje}', True, (255, 255, 255))
        pantalla.blit(texto, (self.texto_x, self.texto_y))

    def texto_final(self):
        mi_fuente_final = self.fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
        pantalla.blit(mi_fuente_final, (60, 200))

    def detectar_colisiones(self, x1, y1, x2, y2):
        distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
        return distancia < 27

    def ejecutar(self):
        se_ejecuta = True
        while se_ejecuta:
            pantalla.blit(fondo, (0, 0))

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    se_ejecuta = False

                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                    sonido_bala = mixer.Sound("disparo.mp3")
                    sonido_bala.play()
                    nueva_bala = Bala(self.jugador.x, self.jugador.y)
                    self.balas.append(nueva_bala)

            self.jugador.mover()

            # Mover y dibujar enemigos
            for enemigo in self.enemigos:
                enemigo.mover()

                if enemigo.y > 500:
                    for e in self.enemigos:
                        e.y = 1000
                    self.texto_final()
                    break

                for bala in self.balas:
                    if self.detectar_colisiones(enemigo.x, enemigo.y, bala.x, bala.y):
                        sonido_colision = mixer.Sound("Golpe.mp3")
                        sonido_colision.play()
                        self.balas.remove(bala)
                        self.puntaje += 1
                        enemigo.x = random.randint(0, 736)
                        enemigo.y = random.randint(20, 200)
                        break

                enemigo.dibujar()

            # Mover y dibujar balas
            for bala in self.balas:
                bala.mover()
                if bala.y < 0:
                    self.balas.remove(bala)
                bala.dibujar()

            self.jugador.dibujar()
            self.mostrar_puntaje()

            pygame.display.update()


# Crear y ejecutar el juego
juego = Juego()
juego.ejecutar()
