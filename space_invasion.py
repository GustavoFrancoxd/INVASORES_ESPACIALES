import pygame
import random
import math
from pygame import mixer

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Invasion Espacial")
        self.icon = pygame.image.load('ovni.png')
        pygame.display.set_icon(self.icon)
        self.background = pygame.image.load('fondo.jpg')
        mixer.music.load('MusicaFondo.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play(-1)
        self.running = True
        self.player = Player()
        self.enemies = [Enemy() for _ in range(8)]
        self.bullets = []
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.game_over_font = pygame.font.Font('freesansbold.ttf', 40)

    def display_score(self):
        score_text = self.font.render(f'Puntaje: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def game_over_text(self):
        game_over_text = self.game_over_font.render("JUEGO TERMINADO", True, (255, 255, 255))
        self.screen.blit(game_over_text, (200, 250))

    def run(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            self.handle_events()
            self.update_game_logic()
            self.render()
            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(-1)
                if event.key == pygame.K_RIGHT:
                    self.player.move(1)
                if event.key == pygame.K_SPACE:
                    self.bullets.append(self.player.shoot())
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    self.player.stop()

    def update_game_logic(self):
        self.player.update_position()
        for bullet in self.bullets[:]:
            bullet.update_position()
            if bullet.y < 0:
                self.bullets.remove(bullet)

        for enemy in self.enemies:
            enemy.update_position()
            if enemy.y > 500:
                for e in self.enemies:
                    e.y = 1000
                self.game_over_text()
                self.running = False

            for bullet in self.bullets[:]:
                if enemy.check_collision(bullet):
                    mixer.Sound("Golpe.mp3").play()
                    self.bullets.remove(bullet)
                    self.score += 1
                    enemy.reset_position()

    def render(self):
        self.player.render(self.screen)
        for bullet in self.bullets:
            bullet.render(self.screen)
        for enemy in self.enemies:
            enemy.render(self.screen)
        self.display_score()


class Player:
    def __init__(self):
        self.image = pygame.image.load('cohete.png')
        self.x = 368
        self.y = 536
        self.x_change = 0

    def move(self, direction):
        self.x_change = direction

    def stop(self):
        self.x_change = 0

    def update_position(self):
        self.x += self.x_change
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

    def shoot(self):
        mixer.Sound("disparo.mp3").play()
        return Bullet(self.x, self.y)

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Enemy:
    def __init__(self):
        self.image = pygame.image.load('enemigo.png')
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)
        self.x_change = 1
        self.y_change = 50

    def update_position(self):
        self.x += self.x_change
        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1
            self.y += self.y_change

    def check_collision(self, bullet):
        distance = math.sqrt(math.pow(self.x - bullet.x, 2) + math.pow(self.y - bullet.y, 2))
        return distance < 27

    def reset_position(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("bala.png")
        self.x = x
        self.y = y
        self.speed = -3

    def update_position(self):
        self.y += self.speed

    def render(self, screen):
        screen.blit(self.image, (self.x + 16, self.y + 10))


if __name__ == "__main__":
    game = Game()
    game.run()
