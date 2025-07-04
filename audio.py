import pygame
from random import randint
import config
pygame.mixer.init()

click_menu = pygame.mixer.Sound('audios/click/clickmenu.wav')
click_menu.set_volume(1)

musicas = {
    'menu1': 'awesomeness.wav',
    'menu2': 'Epic Intro.mp3',
    'game': 'bgGame.mp3',
    'gameover1': 'gameover.wav',
    'gameover2': 'gameover2.wav',
    'gameover3': 'No Hope.mp3',
    'vitoria1': 'vitoria1.ogg',
    'vitoria2': 'vitoria2.mp3'
}

musica_atual = None


def escolher_musica_fundo_e_tocar(musica_escolhida):

    if musica_escolhida == 'menu1':
        pygame.mixer.music.load('audios/menuMusic/awesomeness.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        return 'menu1'
    else:
        pygame.mixer.music.load('audios/menuMusic/Epic Intro.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        return 'menu2'


def parar_musica_fundo():
    pygame.mixer.music.stop()
    #pygame.mixer.music.fadeout(2000)

def tocar_musica_game():
    pygame.mixer.music.load('audios/gameMusic/bgGame.mp3')
    musica_atual = 'game'
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
    explosao = pygame.mixer.Sound('audios/sons_bombas/explosao.mp3')
    explosao.set_volume(0.3)
    explosao.play()

def entoxicar():
    toxico = pygame.mixer.Sound('audios/som_toxico/entoxicando.mp3')
    toxico.set_volume(0.3)
    toxico.play()

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

def tocar_som_congelamento():
    som_escolhido = randint(1,7)

    if som_escolhido == 1:
        congelamento = pygame.mixer.Sound('audios/congelamento/congelamento1.flac')

    elif som_escolhido == 2:
        congelamento = pygame.mixer.Sound('audios/congelamento/congelamento2.flac')

    elif som_escolhido == 3:
        congelamento = pygame.mixer.Sound('audios/congelamento/congelamento3.flac')

    elif som_escolhido == 4:
        congelamento = pygame.mixer.Sound('audios/congelamento/congelamento4.flac')

    elif som_escolhido == 5:
        congelamento = pygame.mixer.Sound('audios/congelamento/congelamento5.flac')

    elif som_escolhido == 6:
        congelamento = pygame.mixer.Sound('audios/congelamento/congelamento6.flac')

    elif som_escolhido == 7:
        congelamento = pygame.mixer.Sound('audios/congelamento/congelamento7.flac')


    congelamento.set_volume(0.1)
    congelamento.play()


# Sons de gameOver
def tocarMusicaGameOver():
    mus_escolhida = randint(1,3)

    if mus_escolhida == 1:
        pygame.mixer.music.load('audios/gameOver/gameOver.wav')
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.5)
        return 'gameover1'
    elif mus_escolhida == 2:
        pygame.mixer.music.load('audios/gameOver/gameOver2.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        return 'gameover2'

    elif mus_escolhida == 3:
        pygame.mixer.music.load('audios/gameOver/No Hope.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        return 'gameover3'

    pygame.mixer.music.set_volume(0.5)

def tocarMusicaVitoria():
    mus_escolhida = randint(2,2)

    if mus_escolhida == 1:
        pygame.mixer.music.load('audios/vitoriaMusic/vitoria1.ogg')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)
        return 'vitoria1'
    elif mus_escolhida == 2:
        pygame.mixer.music.load('audios/vitoriaMusic/vitoria2.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)
        return 'vitoria2'


    pygame.mixer.music.set_volume(0.5)
def tocar_som_explosao_radiacao():
    explosao = pygame.mixer.Sound('audios/som_barrilRadioativo/explosao_barril.wav')
    explosao.set_volume(0.2)
    explosao.play()

def tocar_som_debuff():
    debuff = pygame.mixer.Sound('audios/som_debuff/debuff.wav')
    debuff.set_volume(0.2)
    debuff.play()

def tocar_som_powerup():
    som_escolhido = randint(1,3)

    if som_escolhido == 1:
        powerup = pygame.mixer.Sound('audios/sons_powerUps/powerup1.wav')

    elif som_escolhido == 2:
        powerup = pygame.mixer.Sound('audios/sons_powerUps/powerup2.wav')

    elif som_escolhido == 3:
        powerup = pygame.mixer.Sound('audios/sons_powerUps/powerup3.wav')

    

    powerup.set_volume(0.05)
    powerup.play()

def tocar_som_recuperacao():
    recuperacao = pygame.mixer.Sound('audios/recuperacao/recuperacao.wav')
    recuperacao.set_volume(0.05)
    recuperacao.play()