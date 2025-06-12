import pygame, config
from classes.Player import player





def escolher_fundo(fundoSorteado):
    cor_score = ()
    if fundoSorteado == 1:
        fundo_surf = pygame.image.load('graficos/fundo/fundo1.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))

        cor_score =  (64,64,64)
    if fundoSorteado == 2:
        fundo_surf = pygame.image.load('graficos/fundo/fundo2.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))

        cor_score =  (64,64,64)

    if fundoSorteado == 3:
        fundo_surf = pygame.image.load('graficos/fundo/fundo3.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))

        cor_score =  'white'

    if fundoSorteado == 4:
        fundo_surf = pygame.image.load('graficos/fundo/fundo4.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura)) 

        cor_score =  'white'


    if fundoSorteado == 5:
        fundo_surf = pygame.image.load('graficos/fundo/fundo5.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura)) 

        cor_score =  (64,64,64)


    if fundoSorteado == 6:
        fundo_surf = pygame.image.load('graficos/fundo/fundo6.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))  

        cor_score =  'white'


    if fundoSorteado == 7:
        fundo_surf = pygame.image.load('graficos/fundo/fundo7.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))

        cor_score =  (64,64,64)


    return fundo_surf, cor_score

def mostrar_fundo(fundo):
    config.screen.blit(fundo, (0, 0))


def barcoCheio(mensagem_text, mensagem_text_rect):
    if player.sprite.peso - player.sprite.pesoExtra >= 8:
        config.screen.blit(mensagem_text,mensagem_text_rect)


     