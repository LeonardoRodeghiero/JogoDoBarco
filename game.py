import pygame
from sys import exit
from random import randint, choice
from time import sleep
import config
import audio
from classes.Player import Player
from classes.Moeda import Moeda
from classes.Inimigo import Inimigo, ParticulaRadiacao
from classes.PowerUp import PowerUp
from classes.Debuff import Debuff, ParticulaFumaca
import FuncExternas.funcExternas
from vitoria import vitoria

pygame.init()

import menu

def Jogo():
    musica_escolhida = choice(['menu1', 'menu2'])
    
    if not pygame.mixer.music.get_busy():
        audio.musica_atual = audio.escolher_musica_fundo_e_tocar(musica_escolhida)
    if audio.musica_atual in ['gameover1', 'gameover2', 'gameover3', 'vitoria1', 'vitoria2']:
        audio.musica_atual = audio.escolher_musica_fundo_e_tocar(musica_escolhida)
    
    while True:
        menu.menu.blit(menu.menubg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = config.title_font.render("BOAT GAME", True, "#b68f40")
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.checkForInput(mouse_pos):
                    audio.click_menu.play()
                    return "jogo"
                if options_button.checkForInput(mouse_pos):
                    audio.click_menu.play()
                    return "options"

                if quit_button.checkForInput(mouse_pos):
                    audio.click_menu.play()
                    sleep(0.1)
                    pygame.quit()
                    exit()

        pygame.display.update()

def main():
    from gameover import gameover
    estado = "menu"
    while True:
        if estado == "menu":                    
            pygame.display.set_caption("Menu")
            estado = Jogo()
        if estado == 'jogo':
            pygame.display.set_caption("Catch The Coin")
            estado = play(config.modo_jogo)

        elif estado == "gameover":
            pygame.display.set_caption("Game Over")
            estado = gameover()
        elif estado == "vitoria":
            pygame.display.set_caption("Vitoria")
            estado = vitoria(config.vencedor)
        elif estado == 'options':
            pygame.display.set_caption("Options")
            estado = menu.options()
        elif estado == 'info':
            pygame.display.set_caption("Info")
            estado = menu.info()
        elif estado == "sair":
            break


def play(qtdplayers):

    if qtdplayers == 1:
        import tempo
        audio.parar_musica_fundo()
        audio.tocar_musica_game()
        config.score = 0
        tempo_colisao_Porto = 0
        fundoSorteado = randint(2, 7)
        fundo_atual, cor_score = FuncExternas.funcExternas.escolher_fundo(fundoSorteado)
        camera_x = 0
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

        camera_x = 0

        config.inimigo_group.empty()
        config.moeda_group.empty()
        config.powerup_group.empty()
        config.debuff_group.empty()
        config.area_congelada_group.empty()
        config.area_radioativa_group.empty()
        config.grupo_particulas_gelo.empty()
        player = pygame.sprite.GroupSingle()

        player.empty()
        player.add(Player(config.largura / 2, config.altura))

        def barcoCheio(mensagem_text, mensagem_text_rect):
            if player.sprite.peso - player.sprite.pesoExtra >= 8:
                config.screen.blit(mensagem_text,mensagem_text_rect)


        tempo.resetar_tempo()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                

                if event.type == config.moeda_timer:
                    config.moeda_group.add(Moeda(choice(['ouro', 'prata', 'prata', 'bronze', 'bronze', 'bronze']), camera_x))

                if event.type == config.inimigo_timer:
                    config.inimigo_group.add(Inimigo(choice(['barrilRadioativo','bomba','flecha', 'bomba','flecha']), camera_x))
                    
                if event.type == config.powerup_timer:
                    config.powerup_group.add(PowerUp(choice(['velocidade', 'vida', 'moeda2x', 'tempo', 'pesoExtra', 'invulnerabilidade', 'escudo']), camera_x))
                    
                if event.type == config.debuff_timer:
                    config.debuff_group.add(Debuff(choice(['congelamento', 'lentidao', 'menostempo', 'moedas valem menos']), camera_x))
                    
                if event.type == config.dificuldade_timer:
                    if config.tempo_moeda > 400:
                        config.tempo_moeda = max(config.tempo_moeda - 200, 400)
                        pygame.time.set_timer(config.moeda_timer, config.tempo_moeda)

                    if config.tempo_inimigo > 800:
                        config.tempo_inimigo = max(config.tempo_inimigo - 300, 800)
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
                    
            if len(player) == 0:
                return "gameover"
            
            
            #FuncExternas.funcExternas.mostrar_fundo(fundo_surf)
            for camada in fundo_atual:
                FuncExternas.funcExternas.mostrar_fundo_com_efeito(camada["imagem"], camada['velocidade'], camada['y'], player.sprite.rect.x)

            score_text = config.test_font.render(f'Score: {config.score}', False, cor_score)
            score_text_rect = score_text.get_rect(topright=(config.largura-20, 20))
            config.screen.blit(score_text,score_text_rect)

            mensagem_text = config.mensagem_test_font.render('Barco cheio. Descarregue no porto', False, cor_score)
            mensagem_text_rect = mensagem_text.get_rect(midbottom=(player.sprite.rect.x + 55, config.altura-50))
            
            porto_surf = pygame.image.load('graficos/porto/porto.png')

            porto_mundo_x = config.largura 
            porto_mundo_y = config.altura

            camera_x = player.sprite.rect.x - config.largura // 2

            x_tela_porto = porto_mundo_x - camera_x
            y_tela_porto = porto_mundo_y  

            porto_rect = porto_surf.get_rect(bottomright=(x_tela_porto, y_tela_porto))

            config.screen.blit(porto_surf, porto_rect)
            

            tempo_necessario_Porto = int(player.sprite.peso) * 1000 / 2
            
            if player.sprite.rect.colliderect(porto_rect):

                if tempo_colisao_Porto == 0:  
                    tempo_colisao_Porto = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - tempo_colisao_Porto >= tempo_necessario_Porto:
                    config.score += player.sprite.pontos
                    player.sprite.pontos = 0
                    player.sprite.peso = 0
                else:
                    tempo_restante = tempo_necessario_Porto - (pygame.time.get_ticks() - tempo_colisao_Porto)

                    timer_Porto = config.test_font.render(f'{int(tempo_restante // 1000 + 1)}', False, cor_score)
                    timer_Porto_rect = score_text.get_rect(midbottom=(x_tela_porto - 50, config.altura-80))
                    config.screen.blit(timer_Porto,timer_Porto_rect)

            
            else:
                tempo_colisao_Porto = 0

            barcoCheio(mensagem_text, mensagem_text_rect)
            
            for moeda in config.moeda_group:
                x_tela_moeda = moeda.mundo_x - camera_x
                moeda.rect.x = x_tela_moeda
            config.moeda_group.draw(config.screen)
            config.moeda_group.update()


            for inimigo in config.inimigo_group:
                x_tela_inimigo = inimigo.mundo_x - camera_x
                inimigo.rect.x = x_tela_inimigo

            config.inimigo_group.draw(config.screen)
            config.inimigo_group.update(camera_x)

            for powerup in config.powerup_group:
                x_tela_powerup = powerup.mundo_x - camera_x
                powerup.rect.x = x_tela_powerup

            config.powerup_group.draw(config.screen)
            config.powerup_group.update()

            for debuff in config.debuff_group:
                x_tela_debuff = debuff.mundo_x - camera_x
                debuff.rect.x = x_tela_debuff


            config.debuff_group.draw(config.screen)
            config.debuff_group.update(camera_x)

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

            # Area radioativa
           
            for area in config.area_radioativa_group:
                if pygame.time.get_ticks() - area.tempo_criacao >= area.duracao:
                    area.kill()

            for area in config.area_radioativa_group:
                # Remove se passou o tempo
                tempo_area_radioativa = pygame.time.get_ticks()
                if tempo_area_radioativa - area.tempo_criacao >= area.duracao:
                    area.kill()
                else:
                    # Cria partícula ocasionalmente
                    if randint(0, 10) == 0:  # 1 em 10 frames (pode ajustar)
                        x = randint(area.rect.left, area.rect.right)
                        y = area.rect.top + randint(-5, 5)
                        particula = ParticulaRadiacao((x,y))                    
                        config.grupo_particulas_radiacao.add(particula)

            config.grupo_particulas_radiacao.update()
            config.grupo_particulas_radiacao.draw(config.screen)

            for areaCongelada in config.area_congelada_group:
                x_tela_areaCongelada = areaCongelada.mundo_x - camera_x
                areaCongelada.rect.x = x_tela_areaCongelada

            config.area_congelada_group.draw(config.screen)

            for areaRadioativa in config.area_radioativa_group:
                x_tela_areaRadioativa = areaRadioativa.mundo_x - camera_x
                areaRadioativa.rect.x = x_tela_areaRadioativa

            config.area_radioativa_group.draw(config.screen)
            player.sprite.draw(config.screen)
            player.update()

            pygame.display.update()
            config.clock.tick(60)

    if qtdplayers == 2:
        import tempo
        audio.parar_musica_fundo()
        audio.tocar_musica_game()
        config.score_p1 = 0
        config.score_p2 = 0

        cor_score_p1 = 'blue'
        cor_score_p2 = 'red'
        tempo_colisao_Porto_p1 = 0
        tempo_colisao_Porto_p2 = 0
        ultimo_a_morrer = 0
        cont_morte = 0


        fundoSorteado = randint(2, 7)
        fundo_atual, cor_score= FuncExternas.funcExternas.escolher_fundo_2Players(fundoSorteado)

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
        config.area_radioativa_group.empty()
        config.grupo_particulas_gelo.empty()

        player_group = pygame.sprite.Group()

        posicao_player_1 = config.largura / 2
        posicao_player_1 = posicao_player_1 - posicao_player_1 / 2

        posicao_player_2 = config.largura / 2
        posicao_player_2 = posicao_player_2 + posicao_player_2 / 2

        player_group.empty()
        player_group.add(Player(posicao_player_1, config.altura, 1))
        player_group.add(Player(posicao_player_2, config.altura, 2))
        tempo.resetar_tempo()

        def barcoCheio():
            
            for player in player_group:
                
                if player.peso - player.pesoExtra >= 8:
                    if player.id == 1:
                        mensagem_text = config.mensagem_test_font.render('Barco cheio. Descarregue no porto', False, cor_score_p1)
                        mensagem_text_rect = mensagem_text.get_rect(midbottom=(player.rect.x + 55, config.altura-50))
                    else:
                        mensagem_text = config.mensagem_test_font.render('Barco cheio. Descarregue no porto', False, cor_score_p2)
                        mensagem_text_rect = mensagem_text.get_rect(midbottom=(player.rect.x + 55, config.altura-50))
                    config.screen.blit(mensagem_text,mensagem_text_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()          

                if event.type == config.moeda_timer:
                    config.moeda_group.add(Moeda(choice(['ouro', 'prata', 'prata', 'bronze', 'bronze', 'bronze'])))

                if event.type == config.inimigo_timer:
                    config.inimigo_group.add(Inimigo(choice(['bomba','flecha', 'bomba','flecha', 'barrilRadioativo'])))
                    
                if event.type == config.powerup_timer:
                    config.powerup_group.add(PowerUp(choice(['vida', 'pesoExtra', 'escudo', 'velocidade', 'moeda2x', 'invulnerabilidade'])))
                    
                if event.type == config.debuff_timer:
                    config.debuff_group.add(Debuff(choice(['congelamento', 'lentidao', 'moedas valem menos'])))
                    
                if event.type == config.dificuldade_timer:
                    if config.tempo_moeda > 400:
                        config.tempo_moeda = max(config.tempo_moeda - 200, 400)
                        pygame.time.set_timer(config.moeda_timer, config.tempo_moeda)

                    if config.tempo_inimigo > 800:
                        config.tempo_inimigo = max(config.tempo_inimigo - 300, 800)
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
            
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    for player in player_group:
                        print(f'Vida Atual player {player.id}:{player.vidaAtual}')
            
            if len(player_group) == 1 and cont_morte == 0:
                for player in player_group:
                    if player.id == 1:
                        ultimo_a_morrer = 1
                    if player.id == 2:
                        ultimo_a_morrer = 2
                cont_morte = 1

            if len(player_group) == 0:
                if config.score_p1 > config.score_p2:
                    config.vencedor = 1
                    return "vitoria"
                if config.score_p2 > config.score_p1:
                    config.vencedor = 2
                    return "vitoria"
                if config.score_p1 == config.score_p2:
                    if ultimo_a_morrer == 1:
                        config.vencedor = 1
                        return "vitoria"
                    if ultimo_a_morrer == 2:
                        config.vencedor = 2
                        return "vitoria"
     
            FuncExternas.funcExternas.mostrar_fundo(fundo_atual)

            score_p1_text = config.test_font.render(f'Score: {config.score_p1}', False, cor_score_p1)
            score_p1_text_rect = score_p1_text.get_rect(topleft=(10, 135))
            config.screen.blit(score_p1_text,score_p1_text_rect)

            p1_text = config.test_font.render(f'Jogador 1', False, cor_score_p1)
            p1_text_rect = p1_text.get_rect(topleft=(10, 10))
            config.screen.blit(p1_text, p1_text_rect)

            score_p2_text = config.test_font.render(f'Score: {config.score_p2}', False, cor_score_p2)
            score_p2_text_rect = score_p2_text.get_rect(topright=(config.largura - 10, 135))
            config.screen.blit(score_p2_text,score_p2_text_rect)
            p2_text = config.test_font.render(f'Jogador 2', False, cor_score_p2)
            p2_text_rect = p2_text.get_rect(topright=(config.largura-10, 10))
            config.screen.blit(p2_text, p2_text_rect)

            barcoCheio()

            porto_surf = pygame.image.load('graficos/porto/porto.png')
            porto_rect = porto_surf.get_rect(bottomright=(config.largura, config.altura))
            config.screen.blit(porto_surf, porto_rect)

            for player in player_group:
                if player.id == 1:
                    tempo_necessario_Porto_p1 = int(player.peso) * 1000 / 2

                    if player.rect.colliderect(porto_rect):

                        if tempo_colisao_Porto_p1 == 0:  
                            tempo_colisao_Porto_p1 = pygame.time.get_ticks()
                        elif pygame.time.get_ticks() - tempo_colisao_Porto_p1 >= tempo_necessario_Porto_p1:
                            config.score_p1 += player.pontos
                            player.pontos = 0
                            player.peso = 0
                        else:
                            tempo_restante_p1 = tempo_necessario_Porto_p1 - (pygame.time.get_ticks() - tempo_colisao_Porto_p1)

                            timer_Porto_p1 = config.test_font.render(f'{int(tempo_restante_p1 // 1000 + 1)}', False, cor_score_p1)
                            timer_Porto_rect_p1 = score_p1_text.get_rect(bottomright=(config.largura - 20, config.altura-80))
                            config.screen.blit(timer_Porto_p1,timer_Porto_rect_p1)
                    
                    else:
                        tempo_colisao_Porto_p1 = 0
                else:
                    tempo_necessario_Porto_p2 = int(player.peso) * 1000 / 2

                    if player.rect.colliderect(porto_rect):

                        if tempo_colisao_Porto_p2 == 0:  
                            tempo_colisao_Porto_p2 = pygame.time.get_ticks()
                        elif pygame.time.get_ticks() - tempo_colisao_Porto_p2 >= tempo_necessario_Porto_p2:
                            config.score_p2 += player.pontos
                            player.pontos = 0
                            player.peso = 0
                        else:
                            tempo_restante_p2 = tempo_necessario_Porto_p2 - (pygame.time.get_ticks() - tempo_colisao_Porto_p2)

                            timer_Porto_p2 = config.test_font.render(f'{int(tempo_restante_p2 // 1000 + 1)}', False, cor_score_p2)
                            timer_Porto_rect_p2 = score_p2_text.get_rect(bottomright=(config.largura + 50, config.altura-80))
                            config.screen.blit(timer_Porto_p2,timer_Porto_rect_p2)

                    
                    else:
                        tempo_colisao_Porto_p2 = 0

            #barcoCheio(mensagem_text, mensagem_text_rect)
            
            
            config.moeda_group.draw(config.screen)
            config.moeda_group.update()

            config.inimigo_group.draw(config.screen)
            config.inimigo_group.update()

            config.powerup_group.draw(config.screen)
            config.powerup_group.update()

            config.debuff_group.draw(config.screen)
            config.debuff_group.update()

            estado = tempo.verificar_timer(cor_score, tempo.tempo_total, tempo.tempo_inicio, config.score_p1, config.score_p2)
           
            if estado == "vitoria":
                return "vitoria"

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




            # Area radioativa
            
            for area in config.area_radioativa_group:
                if pygame.time.get_ticks() - area.tempo_criacao >= area.duracao:
                    area.kill()

            for area in config.area_radioativa_group:
                # Remove se passou o tempo
                tempo_area_radioativa = pygame.time.get_ticks()
                if tempo_area_radioativa - area.tempo_criacao >= area.duracao:
                    area.kill()
                else:
                    # Cria partícula ocasionalmente
                    if randint(0, 10) == 0:  # 1 em 10 frames (pode ajustar)
                        x = randint(area.rect.left, area.rect.right)
                        y = area.rect.top + randint(-5, 5)
                        particula = ParticulaRadiacao((x,y))                    
                        config.grupo_particulas_radiacao.add(particula)


            





            config.grupo_particulas_radiacao.update()
            config.grupo_particulas_radiacao.draw(config.screen)



            config.area_congelada_group.draw(config.screen)
            config.area_radioativa_group.draw(config.screen)

            for player in player_group:
                player.draw(config.screen)
                player.update()



            pygame.display.update()
            config.clock.tick(60)

main()

