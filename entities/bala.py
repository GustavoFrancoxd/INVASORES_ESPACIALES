# entities/bala.py (Clase Bala)
import pygame
from config import BULLET_SPEED

class Bala:
    def __init__(self, x, y):
        self.img = pygame.image.load('assets/img/bala.png')
        self.x = x
        self.y = y
        self.velocidad = BULLET_SPEED

    def mover(self):
        self.y += self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.img, (self.x + 16, self.y + 10))