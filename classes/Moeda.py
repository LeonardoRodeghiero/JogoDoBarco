import pygame
from random import randint
import config




class Moeda(pygame.sprite.Sprite):
    def __init__(self, tipo, camera_x=0):
        super().__init__()

        if tipo == 'ouro':
            ouro_1 = pygame.image.load('graficos/moeda/ouro/moedaouro1.png').convert_alpha()
            ouro_2 = pygame.image.load('graficos/moeda/ouro/moedaouro2.png').convert_alpha()
            ouro_3 = pygame.image.load('graficos/moeda/ouro/moedaouro3.png').convert_alpha()
            ouro_4 = pygame.image.load('graficos/moeda/ouro/moedaouro4.png').convert_alpha()
            ouro_5 = pygame.image.load('graficos/moeda/ouro/moedaouro5.png').convert_alpha()
            ouro_6 = pygame.image.load('graficos/moeda/ouro/moedaouro6.png').convert_alpha()
            ouro_7 = pygame.image.load('graficos/moeda/ouro/moedaouro7.png').convert_alpha()
            ouro_8 = pygame.image.load('graficos/moeda/ouro/moedaouro8.png').convert_alpha()
            
            self.frames = [ouro_1, ouro_2, ouro_3, ouro_4, ouro_5, ouro_6, ouro_7, ouro_8]
            self.gravidade = randint(5, 7)
            self.tipo = 'ouro'
        elif tipo == 'prata':
            prata_1 = pygame.image.load('graficos/moeda/prata/moedaprata1.png').convert_alpha()
            prata_2 = pygame.image.load('graficos/moeda/prata/moedaprata2.png').convert_alpha()
            prata_3 = pygame.image.load('graficos/moeda/prata/moedaprata3.png').convert_alpha()
            prata_4 = pygame.image.load('graficos/moeda/prata/moedaprata4.png').convert_alpha()
            prata_5 = pygame.image.load('graficos/moeda/prata/moedaprata5.png').convert_alpha()
            prata_6 = pygame.image.load('graficos/moeda/prata/moedaprata6.png').convert_alpha()
            prata_7 = pygame.image.load('graficos/moeda/prata/moedaprata7.png').convert_alpha()
            prata_8 = pygame.image.load('graficos/moeda/prata/moedaprata8.png').convert_alpha()
            self.frames = [prata_1, prata_2, prata_3, prata_4, prata_5, prata_6, prata_7, prata_8]
            self.gravidade = randint(3, 5)
            self.tipo = 'prata'

        elif tipo == 'bronze':
            bronze_1 = pygame.image.load('graficos/moeda/bronze/moedabronze1.png').convert_alpha()
            bronze_2 = pygame.image.load('graficos/moeda/bronze/moedabronze2.png').convert_alpha()
            bronze_3 = pygame.image.load('graficos/moeda/bronze/moedabronze3.png').convert_alpha()
            bronze_4 = pygame.image.load('graficos/moeda/bronze/moedabronze4.png').convert_alpha()
            bronze_5 = pygame.image.load('graficos/moeda/bronze/moedabronze5.png').convert_alpha()
            bronze_6 = pygame.image.load('graficos/moeda/bronze/moedabronze6.png').convert_alpha()
            bronze_7 = pygame.image.load('graficos/moeda/bronze/moedabronze7.png').convert_alpha()
            bronze_8 = pygame.image.load('graficos/moeda/bronze/moedabronze8.png').convert_alpha()
            self.frames = [bronze_1, bronze_2, bronze_3, bronze_4, bronze_5, bronze_6, bronze_7, bronze_8]
            self.gravidade = randint(2, 4)
            self.tipo = 'bronze'

        self.animacao_index = 0
        self.image = self.frames[self.animacao_index]
        self.rect = self.image.get_rect(midbottom=(randint(camera_x + 9, camera_x + config.largura - 9), randint(-100, 0))) # Pode colocar um numero aleatorio para randomizar a queda das moedas
        self.mundo_x = self.rect.x



    def queda(self):
        self.rect.y += self.gravidade
        

    def destruir(self):
        if self.rect.y >= config.altura + 50:
            self.kill()



    def animacao(self):
        self.animacao_index += 0.1
        if self.animacao_index >= len(self.frames): self.animacao_index = 0
        self.image = self.frames[int(self.animacao_index)]

    def update(self):
        self.animacao()
        self.queda()
        self.destruir()
