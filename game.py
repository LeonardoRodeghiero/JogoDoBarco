import pygame
from sys import exit
from random import randint, choice
import config
from classes.Player import player
from classes.Moeda import Moeda
from classes.Inimigo import Inimigo
from classes.PowerUp import PowerUp


pygame.init()

pygame.display.set_caption("Catch The Coin")




import menu

def Jogo():
    while True:
        menu.menu.blit(menu.menubg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = menu.get_font(80).render("MAIN MENU", True, "#b68f40")
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

                    play()
                if options_button.checkForInput(mouse_pos):
                    menu.options()
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()



def play():
    tempo_total = 2 * 60  
    tempo_inicio = pygame.time.get_ticks()

    def verificar_timer(cor_score):
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

            cor_score =  (64,64,64)


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
    score = 0
    tempo_colisao_Porto = 0

    cont_fundo = 0
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
                config.powerup_group.add(PowerUp(choice(['vida', 'velocidade'])))




        if cont_fundo == 0:
            cont_fundo = 1
            if cont_fundo == 1:
                fundoSorteado = randint(1, 7)
                fundo_surf, cor_score = escolher_fundo(fundoSorteado)

        mostrar_fundo(fundo_surf)



        score_text = config.test_font.render(f'Score: {score}', False, cor_score)
        score_text_rect = score_text.get_rect(topright=(config.largura-20, 20))
        config.screen.blit(score_text,score_text_rect)

        mensagem_text = config.mensagem_test_font.render('Barco cheio. Descarregue no porto', False, cor_score)
        mensagem_text_rect = mensagem_text.get_rect(midbottom=(player.sprite.rect.x + 55, config.altura-50))
        



        porto_surf = pygame.image.load('graficos/porto/porto.png')
        porto_rect = porto_surf.get_rect(bottomright=(config.largura, config.altura+38))
        config.screen.blit(porto_surf, porto_rect)


        
        verificar_timer(cor_score)





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



        if player.sprite.peso >= 8:
            config.screen.blit(mensagem_text,mensagem_text_rect)






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

