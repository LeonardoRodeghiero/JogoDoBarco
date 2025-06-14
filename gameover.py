import pygame
import menu
import config


def gameover():
    while True:
        menu.over.blit(menu.overbg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = menu.get_font(80).render("GAME OVER", True, "#b68f40")
        title_rect = title_text.get_rect(center=(config.largura/2, 100))
        menu.over.blit(title_text, title_rect)

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

                    pygame.display.set_caption("Catch The Coin")
                    return "jogo"
                if menu_button.checkForInput(mouse_pos):

                    pygame.display.set_caption("MENU")
                    return "menu"
                if quitg_button.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()

