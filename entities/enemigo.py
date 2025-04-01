# entities/enemigo.py (Clase Enemigo)
import pygame
import random
from config import SCREEN_WIDTH, ENEMY_SPEED, ENEMY_DROP

class Enemigo:
    def __init__(self, x, y):
        self.img = pygame.image.load('assets/img/enemigo.png')
        self.x = x
        self.y = y
        self.x_cambio = ENEMY_SPEED
        self.y_cambio = ENEMY_DROP

    def mover(self):
        self.x += self.x_cambio
        if self.x <= 0 or self.x >= SCREEN_WIDTH - 64:
            self.x_cambio *= -1
            self.y += self.y_cambio

    def dibujar(self, pantalla):
        pantalla.blit(self.img, (self.x, self.y))