import pygame, config

tempo_total = 2 * 60
tempo_inicio = pygame.time.get_ticks()

def resetar_tempo():
    global tempo_total, tempo_inicio
    tempo_total = tempo_total
    tempo_inicio = pygame.time.get_ticks()


def verificar_timer(cor_score, tempo_total, tempo_inicio, score_p1=0, score_p2=0):
    tempo_decorrido = (pygame.time.get_ticks() - tempo_inicio) // 1000
    tempo_restante = max(0, tempo_total - tempo_decorrido)  # Impede valores negativos
    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    minutos = int(minutos)
    segundos = int(segundos)



    timer_surf = config.test_font.render(f'{minutos:02}:{segundos:02}', False, cor_score)
    timer_rect = timer_surf.get_rect(midtop=(config.largura/2, 20))
    config.screen.blit(timer_surf, timer_rect)


    if tempo_restante == 0 and config.modo_jogo == 1:
        return 'gameover'
    
    if tempo_restante == 0 and config.modo_jogo == 2:
        if score_p1 > score_p2:
            config.vencedor = 1
            return 'vitoria'

        if score_p2 > score_p1:
            config.vencedor = 2
            return 'vitoria'
        
        if score_p1 == score_p2:
            config.vencedor = 3
            return 'vitoria'


def adicionarTempo(segundos):
    global tempo_inicio
    tempo_inicio += segundos * 1000

def retirarTempo(segundos):
    global tempo_inicio
    tempo_inicio -= segundos * 1000