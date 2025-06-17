import pygame, config
from random import randint

pygame.init()
#fumacinha = pygame.Surface((10, 10), pygame.SRCALPHA)
fumacinha = pygame.image.load('graficos/debuffs/congelamento/congelamento_1.png')
#pygame.draw.circle(fumacinha, (200, 240, 255, 100), (5, 5), 5)
fumacinha = pygame.transform.scale(fumacinha, (12, 12))

class ParticulaFumaca(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = fumacinha.copy()
        self.rect = self.image.get_rect(center=pos)
        self.vel_y = -1  # sobe
        self.alpha = 100
    
    def update(self):
        self.rect.y += self.vel_y
        self.alpha -= 2  # vai desaparecendo
        if self.alpha <= 0:
            self.kill()
        else:
            self.image.set_alpha(self.alpha)



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

            self.virou_area = False

            self.duracao_area = 5000
            self.tempo_criacao = None

        if tipo == 'lentidao':
            lentidao_1 = pygame.image.load('graficos/debuffs/lentidao/lentidao_1.png')
            lentidao_2 = pygame.image.load('graficos/debuffs/lentidao/lentidao_2.png')
            lentidao_3 = pygame.image.load('graficos/debuffs/lentidao/lentidao_3.png')
            lentidao_4 = pygame.image.load('graficos/debuffs/lentidao/lentidao_4.png')
            lentidao_5 = pygame.image.load('graficos/debuffs/lentidao/lentidao_5.png')
            lentidao_6 = pygame.image.load('graficos/debuffs/lentidao/lentidao_6.png')
            lentidao_7 = pygame.image.load('graficos/debuffs/lentidao/lentidao_7.png')
            lentidao_8 = pygame.image.load('graficos/debuffs/lentidao/lentidao_8.png')

            self.frames = [lentidao_1, lentidao_2, lentidao_3, lentidao_4, lentidao_5, lentidao_6, lentidao_7, lentidao_8]
            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (30, 30))


        if tipo == 'menostempo':
            rel_quebrado_2 = pygame.image.load('graficos/debuffs/relogioQuebrado/relogioQuebrado_2.png')
            rel_quebrado_3 = pygame.image.load('graficos/debuffs/relogioQuebrado/relogioQuebrado_3.png')
            rel_quebrado_4 = pygame.image.load('graficos/debuffs/relogioQuebrado/relogioQuebrado_4.png')
            rel_quebrado_5 = pygame.image.load('graficos/debuffs/relogioQuebrado/relogioQuebrado_5.png')
            rel_quebrado_6 = pygame.image.load('graficos/debuffs/relogioQuebrado/relogioQuebrado_6.png')
            rel_quebrado_7 = pygame.image.load('graficos/debuffs/relogioQuebrado/relogioQuebrado_7.png')
            rel_quebrado_8 = pygame.image.load('graficos/debuffs/relogioQuebrado/relogioQuebrado_8.png')

            self.frames = [rel_quebrado_2,rel_quebrado_3,rel_quebrado_4,rel_quebrado_5,rel_quebrado_6,rel_quebrado_7,rel_quebrado_8]

            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (30, 30))
        if tipo == 'moedas valem menos':
            moedaDiv2_1 = pygame.image.load('graficos/debuffs/moedaDiv2/moedaDiv2_1.png')
            moedaDiv2_2 = pygame.image.load('graficos/debuffs/moedaDiv2/moedaDiv2_2.png')
            moedaDiv2_3 = pygame.image.load('graficos/debuffs/moedaDiv2/moedaDiv2_3.png')
            moedaDiv2_4 = pygame.image.load('graficos/debuffs/moedaDiv2/moedaDiv2_4.png')
            moedaDiv2_5 = pygame.image.load('graficos/debuffs/moedaDiv2/moedaDiv2_5.png')
            moedaDiv2_6 = pygame.image.load('graficos/debuffs/moedaDiv2/moedaDiv2_6.png')
            moedaDiv2_7 = pygame.image.load('graficos/debuffs/moedaDiv2/moedaDiv2_7.png')
            moedaDiv2_8 = pygame.image.load('graficos/debuffs/moedaDiv2/moedaDiv2_8.png')
            
            self.frames = [moedaDiv2_1,moedaDiv2_2,moedaDiv2_3,moedaDiv2_4,moedaDiv2_5,moedaDiv2_6,moedaDiv2_7,moedaDiv2_8]

            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (30, 30))


        
        self.gravidade = randint(1, 12)
        self.debuff_index = 0
        self.image = self.frames[self.debuff_index]
        self.rect = self.image.get_rect(midbottom=(randint(9, config.largura-9), randint(-100, -1)))
    
    def transformar_em_area(self):
        self.virou_area = True

        area = pygame.sprite.Sprite()
        area.image = pygame.Surface((80, 30), pygame.SRCALPHA)
        area.image.fill((180,240,255,120))
        pygame.draw.rect(area.image, (200, 255, 255), area.image.get_rect(), 2)
        area.rect = area.image.get_rect(midbottom=(self.rect.midbottom))
        area.tempo_criacao = pygame.time.get_ticks()
        area.duracao = 5000

        config.area_congelada_group.add(area)

        self.kill()



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
        if self.tipo == 'congelamento' and not self.virou_area:
            self.rect.y += self.gravidade

            if self.rect.bottom >= config.altura:
                self.transformar_em_area()


        self.animacao()
        self.queda()
        self.destruir()
        