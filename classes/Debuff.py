import pygame, config
from random import randint

pygame.init()

class Debuff(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo

        #A partir daqui começar os ifs para o tipo do debuff

        if tipo == 'congelamento':
            congelamento_1 = pygame.image.load('graficos/debuffs/congelamento/congelamento_1.png')
            congelamento_2 = pygame.image.load('graficos/debuffs/congelamento/congelamento_2.png')
            congelamento_3 = pygame.image.load('graficos/debuffs/congelamento/congelamento_3.png')
            congelamento_4 = pygame.image.load('graficos/debuffs/congelamento/congelamento_4.png')
            congelamento_5 = pygame.image.load('graficos/debuffs/congelamento/congelamento_5.png')
            congelamento_6 = pygame.image.load('graficos/debuffs/congelamento/congelamento_6.png')
            congelamento_7 = pygame.image.load('graficos/debuffs/congelamento/congelamento_7.png')
            congelamento_8 = pygame.image.load('graficos/debuffs/congelamento/congelamento_8.png')
            congelamento_9 = pygame.image.load('graficos/debuffs/congelamento/congelamento_9.png')
            congelamento_10 = pygame.image.load('graficos/debuffs/congelamento/congelamento_10.png')
            congelamento_11 = pygame.image.load('graficos/debuffs/congelamento/congelamento_11.png')
            congelamento_12 = pygame.image.load('graficos/debuffs/congelamento/congelamento_12.png')
            congelamento_13 = pygame.image.load('graficos/debuffs/congelamento/congelamento_13.png')
            congelamento_14 = pygame.image.load('graficos/debuffs/congelamento/congelamento_14.png')

            self.frames = [congelamento_1, congelamento_2, congelamento_3, congelamento_4, congelamento_5, congelamento_6, congelamento_7, congelamento_8, congelamento_9, congelamento_10, congelamento_11, congelamento_12, congelamento_13, congelamento_14]

            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (30, 30))




        self.gravidade = randint(1, 12)
        self.debuff_index = 0
        self.image = self.frames[self.debuff_index]
        self.rect = self.image.get_rect(midbottom=(randint(9, config.largura-9), randint(-100, -1)))
    
    def queda(self):
        self.rect.y += self.gravidade

    def animacao(self):
        self.debuff_index += 0.1
        if self.debuff_index >= len(self.frames): self.debuff_index = 0
        self.image = self.frames[int(self.debuff_index)]

    def destruir(self):
        if self.rect.y >= config.altura + 50:
            self.kill()

    def update(self):
        self.animacao()
        self.queda()
        self.destruir()