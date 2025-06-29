import pygame
import sys
import config
import audio
pygame.init()

# Função para carregar fontes do sistema
def get_font(size):
    return pygame.font.SysFont("Arial", size)


# Função para carregar fontes do sistema
def get_font(size):
    return pygame.font.SysFont("Arial", size)
# Tela principal
over = pygame.display.set_mode((config.largura, config.altura))
overbg = pygame.Surface((config.largura, config.altura))
overbg = pygame.image.load("graficos/fundo/FundosDivididos/fundo7/fundo7.png").convert()

filtro_vermelho = pygame.Surface(overbg.get_size(), pygame.SRCALPHA)
filtro_vermelho.fill((150, 0, 0, 120))  # RGBA - 100 é a transparência


# Classe do botão
class Button:
    def __init__(self, image_default, image_hover, pos, text_input, font, base_color, hovering_color):
        self.image_default = image_default
        self.image_hover = image_hover
        self.image = image_default
        self.rect = self.image.get_rect(center=pos)
        self.text_input = text_input
        self.text = font.render(text_input, True, base_color)
        self.text_rect = self.text.get_rect(center=pos)
        self.base_color = base_color
        self.hovering_color = hovering_color

    def update(self, screen):
        screen.blit(self.image, self.rect)
        if self.text_input != "":
            screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.image = self.image_hover
            self.text = pygame.font.Font(None, 10).render(self.text_input, True, self.hovering_color)
        else:
            self.image = self.image_default
            self.text = pygame.font.Font(None, 10).render(self.text_input, True, self.base_color)


menu = pygame.display.set_mode((config.largura, config.altura))
menubg = pygame.Surface((config.largura, config.altura))
menubg = pygame.image.load("graficos/fundo/FundosDivididos/fundo7/fundo7.png").convert()

def options():
    one_p_default = pygame.transform.scale(pygame.image.load('graficos/botoes/1playerwhite.png').convert_alpha(), (150, 60))
    one_p_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/1playergreen.png').convert_alpha(), (150, 60))
    one_p_button = Button(one_p_default, one_p_hover, (config.largura/2, 250), "", get_font(50), "#d7fcd4", "green")

    two_p_default = pygame.transform.scale(pygame.image.load('graficos/botoes/2playerswhite.png').convert_alpha(), (150, 60))
    two_p_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/2playersgreen.png').convert_alpha(), (150, 60))
    two_p_button = Button(two_p_default, two_p_hover, (config.largura/2, 250), "", get_font(50), "#d7fcd4", "green")
    botao_ativo = config.modo_jogo
    if botao_ativo == 1:
        botao_ativo = one_p_button
    if botao_ativo == 2:
        botao_ativo = two_p_button

    info_default = pygame.transform.scale(pygame.image.load('graficos/botoes/infowhite.png').convert_alpha(), (150, 60))
    info_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/infogreen.png').convert_alpha(), (150, 60))
    info_button = Button(info_default, info_hover, (config.largura/2, 375), "", get_font(50), "#d7fcd4", "green")


    back_default = pygame.transform.scale(pygame.image.load('graficos/botoes/backwhite.png').convert_alpha(), (150, 60))
    back_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/backgreen.png').convert_alpha(), (150, 60))
    back_button = Button(back_default, back_hover, (config.largura/2, 500), "", get_font(50), "#d7fcd4", "green")

    
    while True:
        
        menu.blit(menubg, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        title_text = config.title_font.render("OPTIONS", True, "#b68f40")
        title_rect = title_text.get_rect(center=(config.largura/2, 100))
        mode_text = config.subtitle_font.render("SELECT THE GAMEMODE", True, "#b68f40")
        mode_rect = mode_text.get_rect(center=(config.largura/2, 180))
        menu.blit(title_text, title_rect)
        menu.blit(mode_text, mode_rect)
        
        for button in [botao_ativo, back_button, info_button]:
            button.changeColor(mouse_pos)
            button.update(menu)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_ativo.checkForInput(mouse_pos):
                    audio.click_menu.play()
                    if botao_ativo == one_p_button:
                        botao_ativo = two_p_button
                        config.modo_jogo = 2
                    else:
                        botao_ativo = one_p_button
                        config.modo_jogo = 1
                if back_button.checkForInput(mouse_pos):
                    audio.click_menu.play()

                    return "menu"
                if info_button.checkForInput(mouse_pos):
                    audio.click_menu.play()

                    return "info"

        pygame.display.update()




bg_altura = menubg.get_height()

def info():
    # Gera superfícies de texto
    
    deslocamento_y = 0
    altura_total = 1580  # 40 pixels entre linhas
    sombra_offset = (4, 4)
    cor_sombra = (50, 50, 50, 180)

    def quebra_texto(texto, fonte, largura_max):
        palavras = texto.split(' ')
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            teste_linha = linha_atual + palavra + " "
            largura_teste, _ = fonte.size(teste_linha)
            if largura_teste <= largura_max:
                linha_atual = teste_linha
            else:
                linhas.append(linha_atual)
                linha_atual = palavra + " "

        linhas.append(linha_atual)
        return linhas
    
    while True:
        mouse_pos = pygame.mouse.get_pos()

        back_default = pygame.transform.scale(pygame.image.load('graficos/botoes/backwhite.png').convert_alpha(), (150, 60))
        back_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/backgreen.png').convert_alpha(), (150, 60))
        back_button = Button(back_default, back_hover, (config.largura/2, deslocamento_y+140*13), "", get_font(50), "#d7fcd4", "green")
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEWHEEL:
                deslocamento_y += event.y * 30
                deslocamento_y = max(min(deslocamento_y, 0), -(altura_total - 300))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    audio.click_menu.play()
                    return "options"
        
        config.screen.fill((20, 20, 30))
        for y in range(-bg_altura, 400 + bg_altura, bg_altura):
            pos_y = y + (deslocamento_y % bg_altura)
            config.screen.blit(menubg, (0, pos_y))
        title_text = config.title_font.render("INFO", True, "#b68f40")
        title_rect = title_text.get_rect(center=(config.largura/2, 50+deslocamento_y))
        config.screen.blit(title_text, title_rect)

        

        retangulo_centro = pygame.Rect(75, deslocamento_y+75, config.largura-150, altura_total+75)  # (x, y, largura, altura)

        sombra_rect = retangulo_centro.move(sombra_offset)
        pygame.draw.rect(config.screen, cor_sombra, sombra_rect, border_radius=20)

        pygame.draw.rect(config.screen, (0, 0, 128), retangulo_centro, border_radius=20)


        # JOGADOR
        jogador_back_rect = pygame.Rect(80, deslocamento_y+140, config.largura-160, 100)  # (x, y, largura, altura)
        pygame.draw.rect(config.screen, (65, 105, 225), jogador_back_rect, border_radius=20)
        jogador_text = config.info_title.render('Jogador', False, 'white')
        jogador_rect_text = jogador_text.get_rect(center=(retangulo_centro.centerx, retangulo_centro.top + 40))
        config.screen.blit(jogador_text, jogador_rect_text)

        jogador_surf = pygame.image.load('graficos/barco/barco1.png')
        jogador_rect = jogador_surf.get_rect(center=(150, jogador_back_rect.midleft[1]))
        config.screen.blit(jogador_surf, jogador_rect)

        jogador_text_c = config.info_content.render('Voce tem 3 vidas e seu objetivo eh pegar a maior quantidade de moedas possivel dentro do tempo', False, 'white')
        jogador_rect_c = jogador_text_c.get_rect(topleft=(250, jogador_back_rect.midleft[1] - 60))

        texto_j = 'Voce tem 3 vidas e seu objetivo eh pegar a maior quantidade de moedas possivel dentro do tempo'
        linhas = quebra_texto(texto_j, config.info_content, jogador_back_rect.width - 150)

        for i, linha in enumerate(linhas):
            surface = config.info_content.render(linha, False, 'white')
            y = jogador_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (jogador_rect_c.left + 20, y))

        #MOEDAS
        moeda_back_rect = pygame.Rect(80, deslocamento_y+140*2+30, config.largura-160, 180)  # (x, y, largura, altura)
        pygame.draw.rect(config.screen, (65, 105, 225), moeda_back_rect, border_radius=20)
        moeda_text = config.info_title.render('Moedas', False, 'white')
        moeda_rect_text = moeda_text.get_rect(center=(retangulo_centro.centerx, retangulo_centro.top + 220))
        config.screen.blit(moeda_text, moeda_rect_text)

        moedab_surf = pygame.image.load('graficos/moeda/bronze/moedabronze4.png')
        moedab_surf = pygame.transform.scale(moedab_surf, (30,30))
        moedab_rect = moedab_surf.get_rect(center=(150, moeda_back_rect.midleft[1]-70))
        config.screen.blit(moedab_surf, moedab_rect)

        moedap_surf = pygame.image.load('graficos/moeda/prata/moedaprata4.png')
        moedap_surf = pygame.transform.scale(moedap_surf, (30,30))
        moedap_rect = moedap_surf.get_rect(center=(150, moeda_back_rect.midleft[1]-10))
        config.screen.blit(moedap_surf, moedap_rect)

        moedao_surf = pygame.image.load('graficos/moeda/ouro/moedaouro4.png')
        moedao_surf = pygame.transform.scale(moedao_surf, (30,30))
        moedao_rect = moedao_surf.get_rect(center=(150, moeda_back_rect.midleft[1]+50))
        config.screen.blit(moedao_surf, moedao_rect)

        moedab_text_c = config.info_content.render('Moeda de Bronze bastante comum. Vale 1 ponto', False, 'white')
        moedab_rect_c = moedab_text_c.get_rect(topleft=(250, moeda_back_rect.midleft[1] - 120))

        texto_mb = 'Moeda de Bronze bastante comum. Vale 1 ponto'
        linhas_mb = quebra_texto(texto_mb, config.info_content, moeda_back_rect.width - 150)

        for i, linha in enumerate(linhas_mb):
            surface = config.info_content.render(linha, False, 'white')
            y = moedab_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (moeda_back_rect.left + 100, y))

        moedap_text_c = config.info_content.render('Moeda de Prata de raridade media. Vale 2 pontos', False, 'white')
        moedap_rect_c = moedap_text_c.get_rect(topleft=(250, moeda_back_rect.midleft[1] - 60))

        texto_mp = 'Moeda de Prata de raridade media. Vale 2 pontos'
        linhas_mp = quebra_texto(texto_mp, config.info_content, moeda_back_rect.width - 40)

        for i, linha in enumerate(linhas_mp):
            surface = config.info_content.render(linha, False, 'white')
            y = moedap_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (moeda_back_rect.left + 100, y))

        moedao_text_c = config.info_content.render('Moeda de Ouro muito valiosa. Vale 3 pontos', False, 'white')
        moedao_rect_c = moedao_text_c.get_rect(topleft=(250, moeda_back_rect.midleft[1]))

        texto_mo = 'Moeda de Ouro muito valiosa. Vale 3 pontos'
        linhas_mo = quebra_texto(texto_mo, config.info_content, moeda_back_rect.width - 40)

        for i, linha in enumerate(linhas_mo):
            surface = config.info_content.render(linha, False, 'white')
            y = moedao_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (moeda_back_rect.left + 100, y))


        #PORTO
        porto_back_rect = pygame.Rect(80, deslocamento_y+140*4, config.largura-160, 180)  # (x, y, largura, altura)
        pygame.draw.rect(config.screen, (65, 105, 225), porto_back_rect, border_radius=20)
        porto_text = config.info_title.render('Porto', False, 'white')
        porto_rect_text = porto_text.get_rect(center=(retangulo_centro.centerx, retangulo_centro.top + 470))
        config.screen.blit(porto_text, porto_rect_text)

        porto_surf = pygame.image.load('graficos/porto/porto.png')
        porto_rect = porto_surf.get_rect(center=(200, porto_back_rect.midleft[1]))
        config.screen.blit(porto_surf, porto_rect)

        porto_text_c = config.info_content.render('O porto eh onde voce deve descarregar suas moedas, ja que quanto mais moedas voce tem, mais lento voce fica! Mas cuidado! Quanto mais moedas voce tem, mais tempo demora a descarga no porto', False, 'white')
        porto_rect_c = porto_text_c.get_rect(topleft=(100, porto_back_rect.midleft[1] -100))

        texto_porto = 'O porto eh onde voce deve descarregar suas moedas, ja que quanto mais moedas voce tem, mais lento voce fica! Mas cuidado! Quanto mais moedas voce tem, mais tempo demora a descarga no porto'
        linhas_porto = quebra_texto(texto_porto, config.info_content, porto_back_rect.width - 250)


        for i, linha in enumerate(linhas_porto):
            surface = config.info_content.render(linha, False, 'white')
            y = porto_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (porto_back_rect.left + 250, y))


        #INIMIGOS
        obstaculo_back_rect = pygame.Rect(80, deslocamento_y+140*6, config.largura-160, 180)  # (x, y, largura, altura)
        pygame.draw.rect(config.screen, (65, 105, 225), obstaculo_back_rect, border_radius=20)
        obstaculo_text = config.info_title.render('Obstaculos', False, 'white')
        obstaculo_rect_text = obstaculo_text.get_rect(center=(retangulo_centro.centerx, retangulo_centro.top + 745))
        config.screen.blit(obstaculo_text, obstaculo_rect_text)

        bomba_surf = pygame.image.load('graficos/inimigos/bomba/bomb1.png')
        bomba_rect = bomba_surf.get_rect(center=(160, obstaculo_back_rect.midleft[1]-60))
        config.screen.blit(bomba_surf,bomba_rect)

        flecha_surf = pygame.image.load('graficos/inimigos/flecha/flecha1.png')
        flecha_rect = flecha_surf.get_rect(center=(157, obstaculo_back_rect.midleft[1]-20))
        flecha_surf = pygame.transform.scale(flecha_surf, (16,46))
        config.screen.blit(flecha_surf,flecha_rect)

        barril_surf = pygame.image.load('graficos/inimigos/barrilRadioativo/barrilRadioativo_1.png')
        barril_rect = barril_surf.get_rect(center=(235, obstaculo_back_rect.midleft[1]+150))
        barril_surf = pygame.transform.scale(barril_surf, (29.3,39.8))
        config.screen.blit(barril_surf,barril_rect)


        bomba_text_c = config.info_content.render('Uma bomba que cai de maneira uniforme e esta sempre pronta para explodir', False, 'white')
        bomba_rect_c = bomba_text_c.get_rect(topleft=(250, obstaculo_back_rect.midleft[1] - 110))

        texto_bomba = 'Uma bomba que cai de maneira uniforme e esta sempre pronta para explodir'
        linhas_bomba = quebra_texto(texto_bomba, config.info_content, obstaculo_back_rect.width - 150)

        for i, linha in enumerate(linhas_bomba):
            surface = config.info_content.render(linha, False, 'white')
            y = bomba_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (obstaculo_back_rect.left + 120, y))

        flecha_text_c = config.info_content.render('Uma flecha que cai de forma veloz para perfurar o alvo', False, 'white')
        flecha_rect_c = flecha_text_c.get_rect(topleft=(250, obstaculo_back_rect.midleft[1] - 60))

        texto_flecha = 'Uma flecha que cai de forma veloz para perfurar o alvo'
        linhas_flecha = quebra_texto(texto_flecha, config.info_content, obstaculo_back_rect.width - 150)

        for i, linha in enumerate(linhas_flecha):
            surface = config.info_content.render(linha, False, 'white')
            y = flecha_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (obstaculo_back_rect.left + 120, y))


        barril_text_c = config.info_content.render('Um barril Radioativo que quando cai na agua, cria uma area que mata tudo que a toca por 5 segundos', False, 'white')
        barril_rect_c = barril_text_c.get_rect(topleft=(250, obstaculo_back_rect.midleft[1] - 10))

        texto_barril = 'Um barril Radioativo que quando cai na agua, cria uma area por 5 segundos, que tira 1 vida ao toca-la'
        linhas_barril = quebra_texto(texto_barril, config.info_content, obstaculo_back_rect.width - 150)

        for i, linha in enumerate(linhas_barril):
            surface = config.info_content.render(linha, False, 'white')
            y = barril_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (obstaculo_back_rect.left + 120, y))


        #POWER UPS
        powerups_back_rect = pygame.Rect(80, deslocamento_y+140*8, config.largura-160, 300)  # (x, y, largura, altura)
        pygame.draw.rect(config.screen, (65, 105, 225), powerups_back_rect, border_radius=20)
        powerups_text = config.info_title.render('Poderes', False, 'white')
        powerups_rect_text =    powerups_text.get_rect(center=(retangulo_centro.centerx, retangulo_centro.top + 1020))
        config.screen.blit(powerups_text,powerups_rect_text)

        vida_surf = pygame.image.load('graficos/powerups/vida/vida1.png')
        vida_surf = pygame.transform.scale(vida_surf, (30,30))
        vida_rect = vida_surf.get_rect(center=(160, powerups_back_rect.midleft[1]-120))
        config.screen.blit(vida_surf,vida_rect)

        velocidade_surf = pygame.image.load('graficos/powerups/velocidade/velocidade1.png')
        velocidade_surf = pygame.transform.scale(velocidade_surf, (30,30))
        velocidade_rect = velocidade_surf.get_rect(center=(160, powerups_back_rect.midleft[1]-80))
        config.screen.blit(velocidade_surf,velocidade_rect)

        tempo_surf = pygame.image.load('graficos/powerups/tempo/relogio_1.png')
        tempo_surf = pygame.transform.scale(tempo_surf, (30,30))
        tempo_rect = tempo_surf.get_rect(center=(160, powerups_back_rect.midleft[1]-40))
        config.screen.blit(tempo_surf,tempo_rect)

        moeda2x_surf = pygame.image.load('graficos/powerups/moeda2x/moeda2x_1.png')
        moeda2x_surf = pygame.transform.scale(moeda2x_surf, (30,30))
        moeda2x_rect = moeda2x_surf.get_rect(center=(160, powerups_back_rect.midleft[1]+0))
        config.screen.blit(moeda2x_surf,moeda2x_rect)

        mochila_surf = pygame.image.load('graficos/powerups/mochila/mochila_1.png')
        mochila_surf = pygame.transform.scale(mochila_surf, (30,30))
        mochila_rect = mochila_surf.get_rect(center=(160, powerups_back_rect.midleft[1]+40))
        config.screen.blit(mochila_surf,mochila_rect)

        invulnerabilidade_surf = pygame.image.load('graficos/powerups/invulnerabilidade/cristal_1.png')
        invulnerabilidade_surf = pygame.transform.scale(invulnerabilidade_surf, (13.8,30.3))
        invulnerabilidade_rect = invulnerabilidade_surf.get_rect(center=(160, powerups_back_rect.midleft[1]+80))
        config.screen.blit(invulnerabilidade_surf,invulnerabilidade_rect)

        escudo_surf = pygame.image.load('graficos/powerups/escudo/escudo_1.png')
        escudo_surf = pygame.transform.scale(escudo_surf, (23.5,29.7))
        escudo_rect = escudo_surf.get_rect(center=(160, powerups_back_rect.midleft[1]+120))
        config.screen.blit(escudo_surf,escudo_rect)

        vida_text_c = config.info_content.render('Cura uma vida, se nao estiver com vida cheia', False, 'white')
        vida_rect_c = vida_text_c.get_rect(topleft=(250, powerups_back_rect.midleft[1] - 170))

        texto_vida = 'Cura uma vida, se nao estiver com vida cheia'
        linhas_vida = quebra_texto(texto_vida, config.info_content, powerups_back_rect.width - 150)

        for i, linha in enumerate(linhas_vida):
            surface = config.info_content.render(linha, False, 'white')
            y = vida_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (powerups_back_rect.left + 120, y))

        velocidade_text_c = config.info_content.render('Aumenta a velocidade por um tempo determinado', False, 'white')
        velocidade_rect_c = velocidade_text_c.get_rect(topleft=(250, powerups_back_rect.midleft[1] - 130))

        texto_velocidade = 'Aumenta a velocidade por um tempo determinado'
        linhas_velocidade = quebra_texto(texto_velocidade, config.info_content, powerups_back_rect.width - 150)

        for i, linha in enumerate(linhas_velocidade):
            surface = config.info_content.render(linha, False, 'white')
            y = velocidade_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (powerups_back_rect.left + 120, y))

        tempo_text_c = config.info_content.render('Aumenta o tempo restante em 10 segundos', False, 'white')
        tempo_rect_c = tempo_text_c.get_rect(topleft=(250, powerups_back_rect.midleft[1] - 90))

        texto_tempo = 'Aumenta o tempo restante em 10 segundos'
        linhas_tempo = quebra_texto(texto_tempo, config.info_content, powerups_back_rect.width - 150)

        for i, linha in enumerate(linhas_tempo):
            surface = config.info_content.render(linha, False, 'white')
            y = tempo_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (powerups_back_rect.left + 120, y))

        moeda2x_text_c = config.info_content.render('Moedas valem o dobro por um tempo determinado', False, 'white')
        moeda2x_rect_c = moeda2x_text_c.get_rect(topleft=(250, powerups_back_rect.midleft[1] - 50))

        texto_moeda2x = 'Moedas valem o dobro por um tempo determinado'
        linhas_moeda2x = quebra_texto(texto_moeda2x, config.info_content, powerups_back_rect.width - 150)

        for i, linha in enumerate(linhas_moeda2x):
            surface = config.info_content.render(linha, False, 'white')
            y = moeda2x_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (powerups_back_rect.left + 120, y))

        mochila_text_c = config.info_content.render('Aumenta a capacidade de carregar moedas permanentemente', False, 'white')
        mochila_rect_c = mochila_text_c.get_rect(topleft=(250, powerups_back_rect.midleft[1] - 10))

        texto_mochila = 'Aumenta a capacidade de carregar moedas permanentemente'
        linhas_mochila = quebra_texto(texto_mochila, config.info_content, powerups_back_rect.width - 150)

        for i, linha in enumerate(linhas_mochila):
            surface = config.info_content.render(linha, False, 'white')
            y = mochila_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (powerups_back_rect.left + 120, y))

        invulnerabilidade_text_c = config.info_content.render('Deixa invulneravel a ataques diretos por um tempo determinado(Nao anula areas prejudiciais)', False, 'white')
        invulnerabilidade_rect_c = invulnerabilidade_text_c.get_rect(topleft=(250, powerups_back_rect.midleft[1] +23))

        texto_invulnerabilidade = 'Deixa invulneravel a ataques diretos por um tempo determinado(Nao anula areas prejudiciais)'
        linhas_invulnerabilidade = quebra_texto(texto_invulnerabilidade, config.info_content, powerups_back_rect.width - 150)

        for i, linha in enumerate(linhas_invulnerabilidade):
            surface = config.info_content.render(linha, False, 'white')
            y = invulnerabilidade_rect_c.top + 40 + i * 15  # espaçamento entre linhas
            config.screen.blit(surface, (powerups_back_rect.left + 120, y))

        escudo_text_c = config.info_content.render('Da uma vida extra contra ataques diretos(Nao anula areas prejudiciais)', False, 'white')
        escudo_rect_c = escudo_text_c.get_rect(topleft=(250, powerups_back_rect.midleft[1] +70))

        texto_escudo = 'Da uma vida extra contra ataques diretos(Nao anula areas prejudiciais)'
        linhas_escudo = quebra_texto(texto_escudo, config.info_content, powerups_back_rect.width - 150)

        for i, linha in enumerate(linhas_escudo):
            surface = config.info_content.render(linha, False, 'white')
            y = escudo_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (powerups_back_rect.left + 120, y))



        #DEBUFFS
        debuffs_back_rect = pygame.Rect(80, deslocamento_y+140*11-20, config.largura-160, 200)  # (x, y, largura, altura)
        pygame.draw.rect(config.screen, (65, 105, 225), debuffs_back_rect, border_radius=20)
        debuffs_text = config.info_title.render('Penalidades', False, 'white')
        debuffs_rect_text = debuffs_text.get_rect(center=(retangulo_centro.centerx, retangulo_centro.top + 1440-20))
        config.screen.blit(debuffs_text,debuffs_rect_text)

        lentidao_surf = pygame.image.load('graficos/debuffs/lentidao/lentidao_1.png')
        lentidao_surf = pygame.transform.scale(lentidao_surf, (35,30))
        lentidao_rect = lentidao_surf.get_rect(center=(160, debuffs_back_rect.midleft[1]-60))
        config.screen.blit(lentidao_surf,lentidao_rect)


        moedadiv2_surf = pygame.image.load('graficos/debuffs/moedaDiv2/moedaDiv2_1.png')
        moedadiv2_surf = pygame.transform.scale(moedadiv2_surf, (30,30))
        moedadiv2_rect = moedadiv2_surf.get_rect(center=(160, debuffs_back_rect.midleft[1]-20))
        config.screen.blit(moedadiv2_surf,moedadiv2_rect)

        relogioQuebrado_surf = pygame.image.load('graficos/debuffs/relogioQuebrado/relogioQuebrado_2.png')
        relogioQuebrado_surf = pygame.transform.scale(relogioQuebrado_surf, (30,30))
        relogioQuebrado_rect = relogioQuebrado_surf.get_rect(center=(160, debuffs_back_rect.midleft[1]+20))
        config.screen.blit(relogioQuebrado_surf,relogioQuebrado_rect)

        congelamento_surf = pygame.image.load('graficos/debuffs/congelamento/congelamento_1.png')
        congelamento_surf = pygame.transform.scale(congelamento_surf, (30,30))
        congelamento_rect = congelamento_surf.get_rect(center=(160, debuffs_back_rect.midleft[1]+60))
        config.screen.blit(congelamento_surf,congelamento_rect)

        lentidao_text_c = config.info_content.render('Deixa mais lento por um tempo determinado', False, 'white')
        lentidao_rect_c = lentidao_text_c.get_rect(topleft=(250, debuffs_back_rect.midleft[1] - 110))

        texto_lentidao = 'Deixa mais lento por um tempo determinado'
        linhas_lentidao = quebra_texto(texto_lentidao, config.info_content, debuffs_back_rect.width - 150)

        for i, linha in enumerate(linhas_lentidao):
            surface = config.info_content.render(linha, False, 'white')
            y = lentidao_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (debuffs_back_rect.left + 120, y))

        moedadiv2_text_c = config.info_content.render('Moedas valem menos por um tempo determinado', False, 'white')
        moedadiv2_rect_c = moedadiv2_text_c.get_rect(topleft=(250, debuffs_back_rect.midleft[1] - 70))

        texto_moedadiv2 = 'Moedas valem menos por um tempo determinado'
        linhas_moedadiv2 = quebra_texto(texto_moedadiv2, config.info_content, debuffs_back_rect.width - 150)

        for i, linha in enumerate(linhas_moedadiv2):
            surface = config.info_content.render(linha, False, 'white')
            y = moedadiv2_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (debuffs_back_rect.left + 120, y))

        menostempo_text_c = config.info_content.render('Diminui o tempo restante em 10 segundos', False, 'white')
        menostempo_rect_c = menostempo_text_c.get_rect(topleft=(250, debuffs_back_rect.midleft[1] - 30))

        texto_menostempo = 'Diminui o tempo restante em 10 segundos'
        linhas_menostempo = quebra_texto(texto_menostempo, config.info_content, debuffs_back_rect.width - 150)

        for i, linha in enumerate(linhas_menostempo):
            surface = config.info_content.render(linha, False, 'white')
            y = menostempo_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (debuffs_back_rect.left + 120, y))


        congelamento_text_c = config.info_content.render('No contato direto, congela por 2 segundos. E ao encostar na agua, cria uma area congelada, que ao passar em cima, deixa mais lento', False, 'white')
        congelamento_rect_c = congelamento_text_c.get_rect(topleft=(250, debuffs_back_rect.midleft[1] +10))

        texto_congelamento = 'No contato direto, congela por 2 segundos e se encostar na agua, cria uma area congelada, que ao passar em cima, deixa mais lento'
        linhas_congelamento = quebra_texto(texto_congelamento, config.info_content, debuffs_back_rect.width - 150)

        for i, linha in enumerate(linhas_congelamento):
            surface = config.info_content.render(linha, False, 'white')
            y = congelamento_rect_c.top + 40 + i * 15  # espaçamento entre linhas
            config.screen.blit(surface, (debuffs_back_rect.left + 120, y))


        back_button.changeColor(mouse_pos)
        back_button.update(config.screen)

        


        pygame.display.flip()
