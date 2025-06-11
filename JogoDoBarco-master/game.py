import pygame
from sys import exit
from random import randint, choice
import config
from classes.Player import player
from classes.Moeda import Moeda
from classes.Inimigo import Inimigo
from classes.PowerUp import PowerUp
import FuncExternas.funcExternas

pygame.init()


import menu

def Jogo():
    while True:
        menu.menu.blit(menu.menubg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = menu.get_font(80).render("BOAT GAME", True, "#b68f40")
        title_rect = title_text.get_rect(center=(config.largura/2, 100))
        menu.menu.blit(title_text, title_rect)

        # Carrega imagens normais e de hover
        play_default = pygame.transform.scale(pygame.image.load('playwhite1.png').convert_alpha(), (150, 60))
        play_hover =pygame.transform.scale(pygame.image.load('playgreen1.png').convert_alpha(), (150, 60))

        options_default =pygame.transform.scale(pygame.image.load('optionwhite.png').convert_alpha(),(150, 60))
        options_hover = pygame.transform.scale(pygame.image.load('optiongreen.png').convert_alpha(),(150, 60))

        quit_default = pygame.transform.scale(pygame.image.load('quitwhite.png').convert_alpha(), (150, 60))
        quit_hover = pygame.transform.scale(pygame.image.load('quitgreen.png').convert_alpha(), (150, 60))

        # Cria botões com as duas imagens
        play_button = menu.Button(play_default, play_hover, (config.largura/2, 300), "", menu.get_font(50), "#d7fcd4", "green")
        options_button = menu.Button(options_default, options_hover, (config.largura/2, 400), "", menu.get_font(50), "#d7fcd4", "green")
        quit_button = menu.Button(quit_default, quit_hover, (config.largura/2, 500), "", menu.get_font(50), "#d7fcd4", "green")

        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(menu.menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    pygame.display.set_caption("Catch The Coin")
                    play()
                if options_button.checkForInput(mouse_pos):
                    menu.options()
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()




"""def Jogo():
    while True:
        menu.menu.blit(menu.menubg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = menu.get_font(80).render("BOAT GAME", True, "#b68f40")
        title_rect = title_text.get_rect(center=(config.largura/2, 100))
        menu.menu.blit(title_text, title_rect)

        play_button = menu.Button(None, (config.largura/2, 300), "Play", menu.get_font(50), "#d7fcd4", "green")
        options_button = menu.Button(None, (config.largura/2, 400), "Options", menu.get_font(50), "#d7fcd4", "green")
        quit_button = menu.Button(None, (config.largura/2, 500), "Quit", menu.get_font(50), "#d7fcd4", "green")

        for menu.button in [play_button, options_button, quit_button]:
            menu.button.changeColor(mouse_pos)
            menu.button.update(menu.menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    pygame.display.set_caption("Catch The Coin")
                    play()
                if options_button.checkForInput(mouse_pos):
                    menu.options()
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()

"""
def play():
    tempo_total = 2 * 60  
    tempo_inicio = pygame.time.get_ticks()

    
    
    

    cont_fundo = 0
    score = 0
    tempo_colisao_Porto = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == config.moeda_timer:
                config.moeda_group.add(Moeda(choice(['ouro', 'prata', 'prata', 'bronze', 'bronze', 'bronze'])))

            if event.type == config.inimigo_timer:
                config.inimigo_group.add(Inimigo(choice(['bomba','flecha'])))

            if event.type == config.powerup_timer:
                config.powerup_group.add(PowerUp(choice(['vida', 'velocidade', 'moeda2x', 'tempo'])))




        if cont_fundo == 0:
            cont_fundo = 1
            if cont_fundo == 1:
                fundoSorteado = randint(1, 7)
                fundo_surf, cor_score = FuncExternas.funcExternas.escolher_fundo(fundoSorteado)

        FuncExternas.funcExternas.mostrar_fundo(fundo_surf)



        score_text = config.test_font.render(f'Score: {score}', False, cor_score)
        score_text_rect = score_text.get_rect(topright=(config.largura-20, 20))
        config.screen.blit(score_text,score_text_rect)

        mensagem_text = config.mensagem_test_font.render('Barco cheio. Descarregue no porto', False, cor_score)
        mensagem_text_rect = mensagem_text.get_rect(midbottom=(player.sprite.rect.x + 55, config.altura-50))
        



        porto_surf = pygame.image.load('graficos/porto/porto.png')
        porto_rect = porto_surf.get_rect(bottomright=(config.largura, config.altura+38))
        config.screen.blit(porto_surf, porto_rect)


        
        FuncExternas.funcExternas.verificar_timer(cor_score, tempo_total, tempo_inicio)

        tempo_necessario_Porto = int(player.sprite.peso) * 1000 / 2
        
        if player.sprite.rect.colliderect(porto_rect):

            if tempo_colisao_Porto == 0:  
                tempo_colisao_Porto = pygame.time.get_ticks()
            elif pygame.time.get_ticks() - tempo_colisao_Porto >= tempo_necessario_Porto:
                score += player.sprite.pontos
                player.sprite.pontos = 0
                player.sprite.peso = 0
            else:
                tempo_restante = tempo_necessario_Porto - (pygame.time.get_ticks() - tempo_colisao_Porto)

                timer_Porto = config.test_font.render(f'{int(tempo_restante // 1000 + 1)}', False, cor_score)
                timer_Porto_rect = score_text.get_rect(bottomright=(config.largura, config.altura-80))
                config.screen.blit(timer_Porto,timer_Porto_rect)

        
        else:
            tempo_colisao_Porto = 0      
        

        FuncExternas.funcExternas.barcoCheio(mensagem_text, mensagem_text_rect)
        
        
        config.moeda_group.draw(config.screen)
        config.moeda_group.update()

        config.inimigo_group.draw(config.screen)
        config.inimigo_group.update()

        config.powerup_group.draw(config.screen)
        config.powerup_group.update()


        player.draw(config.screen)
        player.update()



        pygame.display.update()
        config.clock.tick(60)

Jogo()

