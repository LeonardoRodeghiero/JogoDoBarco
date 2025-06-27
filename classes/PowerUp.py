import pygame
from random import randint
import config

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, tipo, camera_x=0):
        super().__init__()

        self.tipo = tipo

        if tipo == 'vida':
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

            self.frames = [vida_1,vida_2,vida_3,vida_4,vida_5,vida_6,vida_7,vida_8,vida_9,vida_10,vida_11,vida_12]

            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (28,28))

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

            
            self.frames = [velocidade_1,velocidade_2,velocidade_3,velocidade_4,velocidade_5,velocidade_6,velocidade_7,velocidade_8,velocidade_9,velocidade_10,velocidade_11,velocidade_12]
            
            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (28,28))

        if tipo == 'moeda2x':
            moeda2x_1 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_1.png')
            moeda2x_2 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_2.png')
            moeda2x_3 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_3.png')
            moeda2x_4 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_4.png')
            moeda2x_5 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_5.png')
            moeda2x_6 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_6.png')
            moeda2x_7 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_7.png')
            moeda2x_8 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_8.png')
            moeda2x_9 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_9.png')
            moeda2x_10 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_10.png')
            moeda2x_11 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_11.png')
            moeda2x_12 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_12.png')
            moeda2x_13 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_13.png')
            moeda2x_14 = pygame.image.load('graficos/powerups/moeda2x/moeda2x_14.png')

            
            self.frames = [moeda2x_1, moeda2x_2,moeda2x_3,moeda2x_4,moeda2x_5,moeda2x_6,moeda2x_7,moeda2x_8,moeda2x_9,moeda2x_10,moeda2x_11,moeda2x_12,moeda2x_13,moeda2x_14]

            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (28,28))

        if tipo == 'tempo':
            tempo_1 = pygame.image.load('graficos/powerups/tempo/relogio_1.png')
            tempo_2 = pygame.image.load('graficos/powerups/tempo/relogio_2.png')
            tempo_3 = pygame.image.load('graficos/powerups/tempo/relogio_3.png')
            tempo_4 = pygame.image.load('graficos/powerups/tempo/relogio_4.png')
            tempo_5 = pygame.image.load('graficos/powerups/tempo/relogio_5.png')
            tempo_6 = pygame.image.load('graficos/powerups/tempo/relogio_6.png')
            tempo_7 = pygame.image.load('graficos/powerups/tempo/relogio_7.png')
            tempo_8 = pygame.image.load('graficos/powerups/tempo/relogio_8.png')
            tempo_9 = pygame.image.load('graficos/powerups/tempo/relogio_9.png')
            tempo_10 = pygame.image.load('graficos/powerups/tempo/relogio_10.png')
            tempo_11 = pygame.image.load('graficos/powerups/tempo/relogio_11.png')
            tempo_12 = pygame.image.load('graficos/powerups/tempo/relogio_12.png')
            tempo_13 = pygame.image.load('graficos/powerups/tempo/relogio_13.png')
            tempo_14 = pygame.image.load('graficos/powerups/tempo/relogio_14.png')

            self.frames = [tempo_1, tempo_2, tempo_3, tempo_4, tempo_5, tempo_6, tempo_7, tempo_8, tempo_9, tempo_10, tempo_11, tempo_12, tempo_13, tempo_14]


            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (28,28))


        if tipo == 'pesoExtra':
            mochila_1 = pygame.image.load('graficos/powerups/mochila/mochila_1.png')
            mochila_2 = pygame.image.load('graficos/powerups/mochila/mochila_2.png')
            mochila_3 = pygame.image.load('graficos/powerups/mochila/mochila_3.png')
            mochila_4 = pygame.image.load('graficos/powerups/mochila/mochila_4.png')
            mochila_5 = pygame.image.load('graficos/powerups/mochila/mochila_5.png')
            mochila_6 = pygame.image.load('graficos/powerups/mochila/mochila_6.png')
            mochila_7 = pygame.image.load('graficos/powerups/mochila/mochila_7.png')
            
            self.frames = [mochila_1, mochila_2, mochila_3, mochila_4, mochila_5, mochila_6, mochila_7]

            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (28,28))

        if tipo == 'invulnerabilidade':
            cristal_1 = pygame.image.load('graficos/powerups/invulnerabilidade/cristal_1.png')
            cristal_2 = pygame.image.load('graficos/powerups/invulnerabilidade/cristal_2.png')
            cristal_3 = pygame.image.load('graficos/powerups/invulnerabilidade/cristal_3.png')
            cristal_4 = pygame.image.load('graficos/powerups/invulnerabilidade/cristal_4.png')

            self.frames = [cristal_1, cristal_2, cristal_3, cristal_4]

            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (13,34))

        if tipo == 'escudo':
            escudo_1 = pygame.image.load('graficos/powerups/escudo/escudo_1.png')
            escudo_2 = pygame.image.load('graficos/powerups/escudo/escudo_2.png')
            escudo_3 = pygame.image.load('graficos/powerups/escudo/escudo_3.png')
            escudo_4 = pygame.image.load('graficos/powerups/escudo/escudo_4.png')
            escudo_5 = pygame.image.load('graficos/powerups/escudo/escudo_5.png')
            escudo_6 = pygame.image.load('graficos/powerups/escudo/escudo_6.png')
            escudo_7 = pygame.image.load('graficos/powerups/escudo/escudo_7.png')
            escudo_8 = pygame.image.load('graficos/powerups/escudo/escudo_8.png')
            escudo_9 = pygame.image.load('graficos/powerups/escudo/escudo_9.png')
            escudo_10 = pygame.image.load('graficos/powerups/escudo/escudo_10.png')

            self.frames = [escudo_1,escudo_2,escudo_3,escudo_4,escudo_5,escudo_6,escudo_7,escudo_8,escudo_9,escudo_10]
            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (28,28))


        self.gravidade = randint(1, 12)

        self.powerup_index = 0

        self.image = self.frames[self.powerup_index]
        self.rect = self.image.get_rect(midbottom=(randint(camera_x + 9, camera_x + config.largura - 9), randint(-100, -1)))
        self.mundo_x = self.rect.x

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
