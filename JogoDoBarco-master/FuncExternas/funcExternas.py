import pygame, config
from classes.Player import player

def verificar_timer(cor_score, tempo_total, tempo_inicio):
    tempo_decorrido = (pygame.time.get_ticks() - tempo_inicio) // 1000
    tempo_restante = max(0, tempo_total - tempo_decorrido)  # Impede valores negativos

    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    minutos = int(minutos)
    segundos = int(segundos)

    timer_surf = config.test_font.render(f'{minutos:02}:{segundos:02}', False, cor_score)
    timer_rect = timer_surf.get_rect(midtop=(config.largura/2, 20))
    config.screen.blit(timer_surf, timer_rect)

    if tempo_restante == 0:
        pygame.quit() # Melhorar a lógica de parada por tempo
        exit()


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
    if player.sprite.peso >= 8:
        config.screen.blit(mensagem_text,mensagem_text_rect)


     