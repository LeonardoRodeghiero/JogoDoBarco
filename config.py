import pygame

pygame.init()
test_font = pygame.font.Font('fonte/Pixeltype.ttf', 50)
mensagem_test_font = pygame.font.Font('fonte/Pixeltype.ttf', 15)

largura = 1000
altura = 600
screen = pygame.display.set_mode((largura, altura))

clock = pygame.time.Clock()




# Timers

moeda_timer = pygame.USEREVENT + 1
pygame.time.set_timer(moeda_timer, 400)

inimigo_timer = pygame.USEREVENT + 2
pygame.time.set_timer(inimigo_timer, 1000)

powerup_timer = pygame.USEREVENT + 3
pygame.time.set_timer(powerup_timer, 2000)


#Grupos


moeda_group = pygame.sprite.Group()

inimigo_group = pygame.sprite.Group()

powerup_group = pygame.sprite.Group()