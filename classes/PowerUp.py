import pygame
from random import randint
import config

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()

        self.tipo = tipo

        if tipo == 'moeda2x':
            vida_1 = pygame.image.load('graficos/powerups/vida/vida1.png')
            vida_2 = pygame.image.load('graficos/powerups/vida/vida2.png')
            vida_3 = pygame.image.load('graficos/powerups/vida/vida3.png')
            vida_4 = pygame.image.load('graficos/powerups/vida/vida4.png')
            vida_5 = pygame.image.load('graficos/powerups/vida/vida5.png')
            vida_6 = pygame.image.load('graficos/powerups/vida/vida6.png')
            vida_7 = pygame.image.load('graficos/powerups/vida/vida7.png')
            vida_8 = pygame.image.load('graficos/powerups/vida/vida8.png')
            vida_9 = pygame.image.load('graficos/powerups/vida/vida9.png')
            vida_10 = pygame.image.load('graficos/powerups/vida/vida10.png')
            vida_11 = pygame.image.load('graficos/powerups/vida/vida11.png')
            vida_12 = pygame.image.load('graficos/powerups/vida/vida12.png')

            vida_1 = pygame.transform.scale2x(vida_1)
            vida_2 = pygame.transform.scale2x(vida_2)
            vida_3 = pygame.transform.scale2x(vida_3)
            vida_4 = pygame.transform.scale2x(vida_4)
            vida_5 = pygame.transform.scale2x(vida_5)
            vida_6 = pygame.transform.scale2x(vida_6)
            vida_7 = pygame.transform.scale2x(vida_7)
            vida_8 = pygame.transform.scale2x(vida_8)
            vida_9 = pygame.transform.scale2x(vida_9)
            vida_10 = pygame.transform.scale2x(vida_10)
            vida_11 = pygame.transform.scale2x(vida_11)
            vida_12 = pygame.transform.scale2x(vida_12)

            self.frames = [vida_1,vida_2,vida_3,vida_4,vida_5,vida_6,vida_7,vida_8,vida_9,vida_10,vida_11,vida_12]

        if tipo == 'velocidade':
            velocidade_1 = pygame.image.load('graficos/powerups/velocidade/velocidade1.png')
            velocidade_2 = pygame.image.load('graficos/powerups/velocidade/velocidade2.png')
            velocidade_3 = pygame.image.load('graficos/powerups/velocidade/velocidade3.png')
            velocidade_4 = pygame.image.load('graficos/powerups/velocidade/velocidade4.png')
            velocidade_5 = pygame.image.load('graficos/powerups/velocidade/velocidade5.png')
            velocidade_6 = pygame.image.load('graficos/powerups/velocidade/velocidade6.png')
            velocidade_7 = pygame.image.load('graficos/powerups/velocidade/velocidade7.png')
            velocidade_8 = pygame.image.load('graficos/powerups/velocidade/velocidade8.png')
            velocidade_9 = pygame.image.load('graficos/powerups/velocidade/velocidade9.png')
            velocidade_10 = pygame.image.load('graficos/powerups/velocidade/velocidade10.png')
            velocidade_11 = pygame.image.load('graficos/powerups/velocidade/velocidade11.png')
            velocidade_12 = pygame.image.load('graficos/powerups/velocidade/velocidade12.png')

            velocidade_1 = pygame.transform.scale2x(velocidade_1)
            velocidade_2 = pygame.transform.scale2x(velocidade_2)
            velocidade_3 = pygame.transform.scale2x(velocidade_3)
            velocidade_4 = pygame.transform.scale2x(velocidade_4)
            velocidade_5 = pygame.transform.scale2x(velocidade_5)
            velocidade_6 = pygame.transform.scale2x(velocidade_6)
            velocidade_7 = pygame.transform.scale2x(velocidade_7)
            velocidade_8 = pygame.transform.scale2x(velocidade_8)
            velocidade_9 = pygame.transform.scale2x(velocidade_9)
            velocidade_10 = pygame.transform.scale2x(velocidade_10)
            velocidade_11 = pygame.transform.scale2x(velocidade_11)
            velocidade_12 = pygame.transform.scale2x(velocidade_12)

            self.frames = [velocidade_1,velocidade_2,velocidade_3,velocidade_4,velocidade_5,velocidade_6,velocidade_7,velocidade_8,velocidade_9,velocidade_10,velocidade_11,velocidade_12]


        self.gravidade = randint(1, 12)

        self.powerup_index = 0

        self.image = self.frames[self.powerup_index]
        self.rect = self.image.get_rect(midbottom=(randint(9, config.largura-9), randint(-100, -1)))


    def queda(self):
        self.rect.y += self.gravidade

    def animacao(self):
        self.powerup_index += 0.1
        if self.powerup_index >= len(self.frames): self.powerup_index = 0
        self.image = self.frames[int(self.powerup_index)]

    def destruir(self):
        if self.rect.y >= config.altura + 50:
            self.kill()


    def update(self):
        self.animacao()
        self.queda()
        self.destruir()
