import pygame

pygame.init()
test_font = pygame.font.Font('fonte/Pixeltype.ttf', 50)
mensagem_test_font = pygame.font.Font('fonte/Pixeltype.ttf', 15)
powerUp_debuff_font = pygame.font.Font('fonte/Pixeltype.ttf', 30)

title_font = pygame.font.Font('fonte/Pixeltype.ttf', 120)
score_font = pygame.font.Font('fonte/Pixeltype.ttf', 80)
score2p_font = pygame.font.Font('fonte/Pixeltype.ttf', 60)

largura = 1000
altura = 600
"""# Obter informações do modo de exibição
infoObject = pygame.display.Info()

# A largura do monitor está em infoObject.current_w
largura = infoObject.current_w

# A altura do monitor está em infoObject.current_h
altura = infoObject.current_h"""


screen = pygame.display.set_mode((largura, altura))


clock = pygame.time.Clock()

modo_jogo = 1
vencedor = 0
score = 0
score_p1 = 0
score_p2 = 0


# Timers
"""tempo_moeda = 400
moeda_timer = pygame.USEREVENT + 1
pygame.time.set_timer(moeda_timer, tempo_moeda)

tempo_inimigo = 1000
inimigo_timer = pygame.USEREVENT + 2
pygame.time.set_timer(inimigo_timer, tempo_inimigo)

tempo_powerUp = 2000
powerup_timer = pygame.USEREVENT + 3
pygame.time.set_timer(powerup_timer, tempo_powerUp)

tempo_debuff = 2000
debuff_timer = pygame.USEREVENT + 4
pygame.time.set_timer(debuff_timer, tempo_debuff)
"""
#Configurações para o aumento de nível gradual

tempo_moeda = 1800
moeda_timer = pygame.USEREVENT + 1
pygame.time.set_timer(moeda_timer, tempo_moeda)

tempo_inimigo = 400
inimigo_timer = pygame.USEREVENT + 2
pygame.time.set_timer(inimigo_timer, tempo_inimigo)

tempo_powerUp = 8000
powerup_timer = pygame.USEREVENT + 3
pygame.time.set_timer(powerup_timer, tempo_powerUp)

tempo_debuff = 8000
debuff_timer = pygame.USEREVENT + 4
pygame.time.set_timer(debuff_timer, tempo_debuff)

dificuldade_timer = pygame.USEREVENT + 5
pygame.time.set_timer(dificuldade_timer, 10000)


#Grupos


moeda_group = pygame.sprite.Group()

inimigo_group = pygame.sprite.Group()

powerup_group = pygame.sprite.Group()

debuff_group = pygame.sprite.Group()

area_congelada_group = pygame.sprite.Group()

area_radioativa_group = pygame.sprite.Group()

grupo_particulas_gelo = pygame.sprite.Group()

grupo_particulas_radiacao = pygame.sprite.Group()