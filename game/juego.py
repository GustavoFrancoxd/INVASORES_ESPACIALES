# game/juego.py (Clase Juego)
import pygame
import random
import math
from entities.jugador import Jugador
from entities.enemigo import Enemigo
from entities.bala import Bala
from config import SCREEN_WIDTH, SCREEN_HEIGHT, COLLISION_DISTANCE

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Invasion Espacial")
        icono = pygame.image.load('assets/img/ovni.png')
        pygame.display.set_icon(icono)
        self.fondo = pygame.image.load('assets/img/Fondo.jpg')
        pygame.mixer.music.load('assets/mp3/MusicaFondo.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.jugador = Jugador(368, 526)
        self.enemigos = [Enemigo(random.randint(0, 736), random.randint(50, 200)) for _ in range(8)]
        self.balas = []
        self.puntaje = 0
        self.fuente = pygame.font.Font('freesansbold.ttf', 32)
        self.fuente_final = pygame.font.Font('freesansbold.ttf', 40)

    def mostrar_puntaje(self):
        texto = self.fuente.render(f'Puntaje: {self.puntaje}', True, (255, 255, 255))
        self.pantalla.blit(texto, (10, 10))

    def texto_final(self):
        mi_fuente_final = self.fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
        self.pantalla.blit(mi_fuente_final, (200, 250))

    def detectar_colisiones(self, x1, y1, x2, y2):
        distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distancia < COLLISION_DISTANCE

    def ejecutar(self):
        se_ejecuta = True
        while se_ejecuta:
            self.pantalla.blit(self.fondo, (0, 0))
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    se_ejecuta = False
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                    sonido_bala = pygame.mixer.Sound("assets/mp3/disparo.mp3")
                    sonido_bala.play()
                    self.balas.append(Bala(self.jugador.x, self.jugador.y))
            self.jugador.mover()
            for enemigo in self.enemigos:
                enemigo.mover()
                if enemigo.y > 500:
                    for e in self.enemigos:
                        e.y = 1000
                    self.texto_final()
                    break
                for bala in self.balas:
                    if self.detectar_colisiones(enemigo.x, enemigo.y, bala.x, bala.y):
                        sonido_colision = pygame.mixer.Sound("assets/mp3/Golpe.mp3")
                        sonido_colision.play()
                        self.balas.remove(bala)
                        self.puntaje += 1
                        enemigo.x = random.randint(0, 736)
                        enemigo.y = random.randint(20, 200)
                        break
                enemigo.dibujar(self.pantalla)
            for bala in self.balas:
                bala.mover()
                if bala.y < 0:
                    self.balas.remove(bala)
                bala.dibujar(self.pantalla)
            self.jugador.dibujar(self.pantalla)
            self.mostrar_puntaje()
            pygame.display.update()