import pygame, config

tempo_total = 2 * 60  
tempo_inicio = pygame.time.get_ticks()

def resetar_tempo():
    global tempo_total, tempo_inicio
    tempo_total = 2 * 60
    tempo_inicio = pygame.time.get_ticks()


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
        from gameOver import gameover
        gameover()


def adicionarTempo(segundos):
    global tempo_inicio
    tempo_inicio += segundos * 1000