# entities/bala.py (Clase Bala)
import pygame
from config import BULLET_SPEED

class Bala:
    def __init__(self, x: int, y: int) -> None:
        """Inicializa una bala con su imagen y posición."""
        self.img = pygame.image.load('assets/img/bala.png')
        self.x = x
        self.y = y
        self.velocidad = BULLET_SPEED

    def mover(self) -> None:
        """Mueve la bala hacia arriba."""
        self.y += self.velocidad

    def dibujar(self, pantalla: pygame.Surface) -> None:
        """Dibuja la bala en la pantalla."""
        pantalla.blit(self.img, (self.x + 16, self.y + 10))
