import pygame
import menu
import config
import audio
from time import sleep
def vitoria(vencedor):
    audio.musica_atual = audio.tocarMusicaVitoria()

    while True:
        config.screen.blit(menu.menubg, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        if vencedor == 1:
            config.screen.blit(menu.menubg, (0, 0))

            title_text = config.title_font.render(f"Vitoria do jogador {vencedor}", False, 'blue')
            title_rect = title_text.get_rect(center=(config.largura/2, 100))
        if vencedor == 2:
            config.screen.blit(menu.menubg, (0, 0))

            title_text = config.title_font.render(f"Vitoria do jogador {vencedor}", False, 'red')
            title_rect = title_text.get_rect(center=(config.largura/2, 100))
        if vencedor == 3:
            config.screen.blit(menu.menubg, (0, 0))

            title_text = config.title_font.render("Empate", False, (64,64,64))
            title_rect = title_text.get_rect(center=(config.largura/2, 100))
        
        config.screen.blit(title_text, title_rect)


        score_p1_text = config.score2p_font.render(f"Score jogador 1: {config.score_p1}", False, 'blue')
        score_p1_rect = score_p1_text.get_rect(center=(config.largura/2 - config.largura/2/2, 200))
        config.screen.blit(score_p1_text, score_p1_rect)

        score_p2_text = config.score2p_font.render(f"Score jogador 2: {config.score_p2}", False, 'red')
        score_p2_rect = score_p2_text.get_rect(center=(config.largura/2 + config.largura/2/2, 200))
        config.screen.blit(score_p2_text, score_p2_rect)
        # Carrega imagens normais e de hover
        restart_default = pygame.transform.scale(pygame.image.load('graficos/botoes/restartblack.png').convert_alpha(), (150, 60))
        restart_hover =pygame.transform.scale(pygame.image.load('graficos/botoes/restartgreen.png').convert_alpha(), (150, 60))

        menu_default =pygame.transform.scale(pygame.image.load('graficos/botoes/menublack.png').convert_alpha(),(150, 60))
        menu_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/menugreen.png').convert_alpha(), (150, 60))

        quitg_default = pygame.transform.scale(pygame.image.load('graficos/botoes/quitblack.png').convert_alpha(), (150, 60))
        quitg_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/quitgreen2.png').convert_alpha(), (150, 60))

        # Cria botões com as duas imagens
        restart_button = menu.Button(restart_default, restart_hover, (config.largura/2, 300), "", menu.get_font(50), "#d7fcd4", "green")
        menu_button = menu.Button(menu_default, menu_hover, (config.largura/2, 400), "", menu.get_font(50), "#d7fcd4", "green")
        quitg_button = menu.Button(quitg_default, quitg_hover, (config.largura/2, 500), "", menu.get_font(50), "#d7fcd4", "green")

        for button in [restart_button, menu_button, quitg_button]:
            button.changeColor(mouse_pos)
            button.update(menu.over)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.checkForInput(mouse_pos):
                    audio.click_menu.play()

                    return "jogo"
                if menu_button.checkForInput(mouse_pos):
                    audio.click_menu.play()
                    return "menu"
                if quitg_button.checkForInput(mouse_pos):
                    audio.click_menu.play()
                    sleep(0.1)

                    pygame.quit()
                    exit()

        pygame.display.update()

