import pygame, config
from random import randint

pygame.init()

class Debuff(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo

        #A partir daqui começar os ifs para o tipo do debuff


        self.gravidade = randint(1, 12)
        self.debuff_index = 0

    
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