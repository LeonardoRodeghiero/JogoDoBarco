import pygame
from sys import exit
from random import randint, choice
from time import sleep
import config
import audio
from classes.Player import player
from classes.Player import player, Player
from classes.Moeda import Moeda
from classes.Inimigo import Inimigo
from classes.PowerUp import PowerUp
from classes.Debuff import Debuff, ParticulaFumaca
import FuncExternas.funcExternas


pygame.init()
    

import menu

def Jogo():
    audio.escolher_musica_fundo_e_tocar()

    while True:
        menu.menu.blit(menu.menubg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = menu.get_font(80).render("BOAT GAME", True, "#b68f40")
        title_rect = title_text.get_rect(center=(config.largura/2, 100))
        menu.menu.blit(title_text, title_rect)

        # Carrega imagens normais e de hover
        play_default = pygame.transform.scale(pygame.image.load('graficos/botoes/playwhite1.png').convert_alpha(), (150, 60))
        play_hover =pygame.transform.scale(pygame.image.load('graficos/botoes/playgreen1.png').convert_alpha(), (150, 60))

        options_default =pygame.transform.scale(pygame.image.load('graficos/botoes/optionwhite.png').convert_alpha(),(150, 60))
        options_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/optiongreen.png').convert_alpha(),(150, 60))

        quit_default = pygame.transform.scale(pygame.image.load('graficos/botoes/quitwhite.png').convert_alpha(), (150, 60))
        quit_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/quitgreen.png').convert_alpha(), (150, 60))

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
                    audio.click_menu.play()
                    return "jogo"
                if options_button.checkForInput(mouse_pos):
                    audio.click_menu.play()
                    menu.options()

                if quit_button.checkForInput(mouse_pos):
                    audio.click_menu.play()
                    sleep(0.1)
                    pygame.quit()
                    exit()

        pygame.display.update()








"""def Jogo():
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
"""

def main():
    from gameover import gameover
    estado = "menu"
    while True:
        if estado == "menu":                    
            pygame.display.set_caption("Menu")
            estado = Jogo()
        if estado == 'jogo':
            pygame.display.set_caption("Catch The Coin")
            estado = play()

        elif estado == "gameover":
            pygame.display.set_caption("Game Over")
            estado = gameover()
        elif estado == "sair":
            break


def play():
    import tempo
    audio.parar_musica_fundo()
    audio.tocar_musica_game()
    score = 0
    tempo_colisao_Porto = 0
    fundoSorteado = randint(2, 7)
    fundo_atual, cor_score = FuncExternas.funcExternas.escolher_fundo(fundoSorteado)

    #reset dos timers
    config.tempo_moeda = 1800
    pygame.time.set_timer(config.moeda_timer, 0)
    pygame.time.set_timer(config.moeda_timer, config.tempo_moeda)

    config.tempo_inimigo = 3600
    pygame.time.set_timer(config.inimigo_timer, 0)
    pygame.time.set_timer(config.inimigo_timer, config.tempo_inimigo)

    config.tempo_powerUp = 8000
    pygame.time.set_timer(config.powerup_timer, 0)
    pygame.time.set_timer(config.powerup_timer, config.tempo_powerUp)

    config.tempo_debuff = 8000
    pygame.time.set_timer(config.debuff_timer, 0)
    pygame.time.set_timer(config.debuff_timer, config.tempo_debuff)



    config.inimigo_group.empty()
    config.moeda_group.empty()
    config.powerup_group.empty()
    config.debuff_group.empty()
    config.area_congelada_group.empty()
    config.grupo_particulas_gelo.empty()
    player.empty()
    player.add(Player())
    tempo.resetar_tempo()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            

            if event.type == config.moeda_timer:
                config.moeda_group.add(Moeda(choice(['ouro', 'prata', 'prata', 'bronze', 'bronze', 'bronze'])))

            if event.type == config.inimigo_timer:
                config.inimigo_group.add(Inimigo(choice(['bomba','flecha', 'barrilRadioativo'])))
            
            if event.type == config.powerup_timer:
                config.powerup_group.add(PowerUp(choice(['vida', 'velocidade', 'moeda2x', 'tempo', 'pesoExtra', 'invulnerabilidade', 'escudo'])))
            if event.type == config.debuff_timer:
                config.debuff_group.add(Debuff(choice(['congelamento', 'lentidao', 'menostempo', 'moedas valem menos'])))
                
            if event.type == config.dificuldade_timer:
                if config.tempo_moeda > 200:
                    config.tempo_moeda = max(config.tempo_moeda - 200, 200)
                    pygame.time.set_timer(config.moeda_timer, config.tempo_moeda)

                if config.tempo_inimigo > 500:
                    config.tempo_inimigo = max(config.tempo_inimigo - 300, 500)
                    pygame.time.set_timer(config.inimigo_timer, config.tempo_inimigo)

                if config.tempo_powerUp > 4000:
                    config.tempo_powerUp = max(config.tempo_powerUp - 450, 4000)
                    pygame.time.set_timer(config.powerup_timer, config.tempo_powerUp)

                if config.tempo_debuff > 3000:
                    config.tempo_debuff = max(config.tempo_debuff - 550, 3000)
                    pygame.time.set_timer(config.debuff_timer, config.tempo_debuff)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                print("=== STATUS DOS TIMERS ===")
                print(f"Moeda: {config.tempo_moeda} ms")
                print(f"Inimigo: {config.tempo_inimigo} ms")
                print(f"PowerUp: {config.tempo_powerUp} ms")
                print(f"Debuff: {config.tempo_debuff} ms")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                print("=== STATUS DO Jogador ===")
                print(f"velocidade: {player.sprite.velocidade}")
                print(f"Vida: {player.sprite.vidaAtual}")
                print(f"Debuffs Ativos: {player.sprite.debuffsAtivos}")
                

        if player.sprite.vidaAtual <= 0:
            return "gameover"
        
        
        #FuncExternas.funcExternas.mostrar_fundo(fundo_surf)
        for camada in fundo_atual:
            FuncExternas.funcExternas.mostrar_fundo_com_efeito(camada["imagem"], camada['velocidade'], camada['y'], player.sprite.rect.x)





        score_text = config.test_font.render(f'Score: {score}', False, cor_score)
        score_text_rect = score_text.get_rect(topright=(config.largura-20, 20))
        config.screen.blit(score_text,score_text_rect)

        mensagem_text = config.mensagem_test_font.render('Barco cheio. Descarregue no porto', False, cor_score)
        mensagem_text_rect = mensagem_text.get_rect(midbottom=(player.sprite.rect.x + 55, config.altura-50))
        



        porto_surf = pygame.image.load('graficos/porto/porto.png')
        porto_rect = porto_surf.get_rect(bottomright=(config.largura, config.altura+38))
        config.screen.blit(porto_surf, porto_rect)

        
        

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

        config.debuff_group.draw(config.screen)
        config.debuff_group.update()

        estado = tempo.verificar_timer(cor_score, tempo.tempo_total, tempo.tempo_inicio)
        if estado == "gameover":
            return "gameover"


        for area in config.area_congelada_group:
            if pygame.time.get_ticks() - area.tempo_criacao >= area.duracao:
                area.kill()

        for area in config.area_congelada_group:
            # Remove se passou o tempo
            tempo_area = pygame.time.get_ticks()
            if tempo_area - area.tempo_criacao >= area.duracao:
                area.kill()
            else:
                # Cria partícula ocasionalmente
                if randint(0, 10) == 0:  # 1 em 10 frames (pode ajustar)
                    x = randint(area.rect.left, area.rect.right)
                    y = area.rect.top + randint(-5, 5)
                    particula = ParticulaFumaca((x,y))                    
                    config.grupo_particulas_gelo.add(particula)

        config.grupo_particulas_gelo.update()
        config.grupo_particulas_gelo.draw(config.screen)

        config.area_congelada_group.draw(config.screen)
        player.draw(config.screen)
        player.update()



        pygame.display.update()
        config.clock.tick(60)

main()
