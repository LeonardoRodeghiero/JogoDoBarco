import pygame
from random import randint
import config
pygame.mixer.init()

click_menu = pygame.mixer.Sound('audios/click/clickmenu.wav')
click_menu.set_volume(1)




def escolher_musica_fundo_e_tocar():
    musica_escolhida = randint(1, 2)

    if musica_escolhida == 1:
        pygame.mixer.music.load('audios/menuMusic/awesomeness.wav')
    else:
        pygame.mixer.music.load('audios/menuMusic/Epic Intro.mp3')

    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def parar_musica_fundo():
    pygame.mixer.music.stop()
    #pygame.mixer.music.fadeout(2000)

def tocar_musica_game():
    pygame.mixer.music.load('audios/gameMusic/bgGame.mp3')

    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

def escolher_som_moeda_e_tocar():
    som_moeda_escolhido = randint(1, 10)

    if som_moeda_escolhido == 1:
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin1.wav')
        som_moeda.set_volume(0.05)
    elif som_moeda_escolhido == 2:
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin2.wav')
        som_moeda.set_volume(0.05)
    elif som_moeda_escolhido == 3:
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin3.wav')
        som_moeda.set_volume(0.05)
    elif som_moeda_escolhido == 4:
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin4.wav')
        som_moeda.set_volume(0.05)
    elif som_moeda_escolhido == 5:
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin5.wav')
        som_moeda.set_volume(0.05)
    elif som_moeda_escolhido == 6:
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin6.wav')
        som_moeda.set_volume(0.05)
    elif som_moeda_escolhido == 7:
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin7.wav')
        som_moeda.set_volume(0.05)
    elif som_moeda_escolhido == 8 :
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin8.wav')
        som_moeda.set_volume(0.05)
    elif som_moeda_escolhido == 9:
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin9.wav')
        som_moeda.set_volume(0.05)
    elif som_moeda_escolhido == 10:
        som_moeda = pygame.mixer.Sound('audios/sons_moedas/coin10.wav')
        som_moeda.set_volume(0.05)

    som_moeda.play()


def tocar_som_explosao():
    explosao = pygame.mixer.Sound('audios/sons_bombas/explosao.wav')
    explosao.set_volume(0.1)
    explosao.play()

"""def tocar_som_queda_bomba(inimigo):
    som_queda = pygame.mixer.Sound('audios/sons_bombas/dropbomb-4seconds.mp3')
    som_queda.set_volume(0.005)

    if inimigo.tipo == 'bomba':
        som_queda.play()
        if inimigo.rect.centery >= config.altura:
            som_queda.stop()"""

def tocar_som_flechada():
    flechada = pygame.mixer.Sound('audios/flecha/flecha.ogg')
    flechada.set_volume(0.2)
    flechada.play()

