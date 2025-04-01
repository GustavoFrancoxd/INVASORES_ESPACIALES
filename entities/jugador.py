# entities/jugador.py (Clase Jugador)
import pygame
from config import SCREEN_WIDTH, PLAYER_SPEED


class Jugador:
    def __init__(self, x, y):
        self.img = pygame.image.load('assets/img/cohete.png')
        self.x = x
        self.y = y
        self.x_cambio = 0

    def mover(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_cambio = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.x_cambio = PLAYER_SPEED
        else:
            self.x_cambio = 0

        self.x += self.x_cambio
        self.x = max(0, min(self.x, SCREEN_WIDTH - 64))

    def dibujar(self, pantalla):
        pantalla.blit(self.img, (self.x, self.y))