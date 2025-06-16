import pygame
from random import randint, choice
import config


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()

        self.tipo = tipo

        if tipo == 'bomba':
            bomb_1 = pygame.image.load('graficos/inimigos/bomba/bomb1.png').convert_alpha()
            bomb_2 = pygame.image.load('graficos/inimigos/bomba/bomb2.png').convert_alpha()
            bomb_3 = pygame.image.load('graficos/inimigos/bomba/bomb3.png').convert_alpha()
            bomb_4 = pygame.image.load('graficos/inimigos/bomba/bomb4.png').convert_alpha()
            bomb_5 = pygame.image.load('graficos/inimigos/bomba/bomb5.png').convert_alpha()
            bomb_6 = pygame.image.load('graficos/inimigos/bomba/bomb6.png').convert_alpha()

            self.frames = [bomb_1, bomb_2, bomb_3, bomb_4, bomb_5, bomb_6]

            self.bomb_index = 0

            self.image = self.frames[self.bomb_index]

            inicio = randint(-100, 0)
            inicioPositivo = inicio * -1
            distanciaApercorrer = inicioPositivo + config.altura - 250
            self.distanciaDeTroca = distanciaApercorrer // 6
            self.rect = self.image.get_rect(midbottom=((randint(9, config.largura-9), inicio)))
            self.gravidade = randint(1, 12)






        elif tipo == 'flecha':
            flecha_1 = pygame.image.load('graficos/inimigos/flecha/flecha1.png').convert_alpha()
            flecha_2 = pygame.image.load('graficos/inimigos/flecha/flecha2.png').convert_alpha()
            flecha_3 = pygame.image.load('graficos/inimigos/flecha/flecha3.png').convert_alpha()
            flecha_4 = pygame.image.load('graficos/inimigos/flecha/flecha4.png').convert_alpha()
            
            flecha_1 = pygame.transform.scale2x(flecha_1)
            flecha_2 = pygame.transform.scale2x(flecha_2)
            flecha_3 = pygame.transform.scale2x(flecha_3)
            flecha_4 = pygame.transform.scale2x(flecha_4)


            self.frames = [flecha_1,flecha_2,flecha_3,flecha_4]


            self.flecha_index = 0
            self.image = self.frames[self.flecha_index]

            inicio = randint(-100, 0)
            self.rect = self.image.get_rect(midbottom=((randint(9, config.largura-9), inicio)))
            self.gravidade = randint(1, 4)
            self.velocidadeFlecha = choice([0.1, 0.2, 0.3, 0.4, 0.5])

        elif tipo == 'barrilRadioativo':
            barril_1 = pygame.image.load('graficos/inimigos/barrilRadioativo/barrilRadioativo_1.png').convert_alpha()
            barril_2 = pygame.image.load('graficos/inimigos/barrilRadioativo/barrilRadioativo_2.png').convert_alpha()
            barril_3 = pygame.image.load('graficos/inimigos/barrilRadioativo/barrilRadioativo_3.png').convert_alpha()
            barril_4 = pygame.image.load('graficos/inimigos/barrilRadioativo/barrilRadioativo_4.png').convert_alpha()
            barril_5 = pygame.image.load('graficos/inimigos/barrilRadioativo/barrilRadioativo_5.png').convert_alpha()


            self.barril_index = 0

            self.frames = [barril_1,barril_2,barril_3,barril_4,barril_5]


            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (30,35))

            self.image = self.frames[self.barril_index]

            inicio = randint(-100, 0)
            self.rect = self.image.get_rect(midbottom=((randint(9, config.largura-9), inicio)))
            self.gravidade = randint(1, 12)


    def queda(self):
        if self.tipo == 'flecha':
            self.gravidade += self.velocidadeFlecha
            self.rect.y += self.gravidade
        if self.tipo == 'bomba':
            self.rect.y += self.gravidade
        if self.tipo == 'barrilRadioativo':
            self.rect.y += self.gravidade

    def destruir(self):
        if self.rect.y >= config.altura + 50:
            self.kill()



    def animacao(self):
        if self.tipo == 'bomba' and self.rect.y >= self.distanciaDeTroca:
            self.bomb_index += 1
            self.distanciaDeTroca += self.distanciaDeTroca
            self.image = self.frames[int(self.bomb_index)]

        if self.tipo == 'flecha':
            self.flecha_index += 0.1
            if self.flecha_index >= len(self.frames): self.flecha_index = 0
            self.image = self.frames[int(self.flecha_index)]

        if self.tipo == 'barrilRadioativo':
            self.barril_index += 0.1
            if self.barril_index >= len(self.frames): self.barril_index = 0
            self.image = self.frames[int(self.barril_index)]


    def update(self):
        self.animacao()
        self.queda()
        self.destruir()


