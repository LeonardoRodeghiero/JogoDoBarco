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

def optionsReal():
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
        
        for button in [botao_ativo, back_button]:
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

        pygame.display.update()


# Lista de textos de exemplo
textos = [
    f"Parágrafo {i+1}: Esse é um exemplo de rolagem de texto com Pygame."
    for i in range(30)
]

bg_altura = menubg.get_height()

def options():
    # Gera superfícies de texto
    
    deslocamento_y = 0
    altura_total = 4000  # 40 pixels entre linhas
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEWHEEL:
                deslocamento_y += event.y * 30
                deslocamento_y = max(min(deslocamento_y, 0), -(altura_total - 400))

        config.screen.fill((20, 20, 30))
        for y in range(-bg_altura, 400 + bg_altura, bg_altura):
            pos_y = y + (deslocamento_y % bg_altura)
            config.screen.blit(menubg, (0, pos_y))

        


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

        jogador_text_c = config.info_content.render('Voce tem 3 vidas e seu objetivo eh pegar a maior quantidade de moedas possivel', False, 'white')
        jogador_rect_c = jogador_text_c.get_rect(topleft=(250, jogador_back_rect.midleft[1] - 60))

        texto_j = 'Voce tem 3 vidas e seu objetivo eh pegar a maior quantidade de moedas possivel'
        linhas = quebra_texto(texto_j, config.info_content, jogador_rect_c.width - 40)

        for i, linha in enumerate(linhas):
            surface = config.info_content.render(linha, False, 'white')
            y = jogador_rect_c.top + 40 + i * 30  # espaçamento entre linhas
            config.screen.blit(surface, (jogador_rect_c.left + 20, y))

        #MOEDAS
        moeda_back_rect = pygame.Rect(80, deslocamento_y+140*2, config.largura-160, 180)  # (x, y, largura, altura)
        pygame.draw.rect(config.screen, (65, 105, 225), moeda_back_rect, border_radius=20)
        moeda_text = config.info_title.render('Moedas', False, 'white')
        moeda_rect_text = moeda_text.get_rect(center=(retangulo_centro.centerx, retangulo_centro.top + 190))
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
        linhas_mb = quebra_texto(texto_mb, config.info_content, moeda_back_rect.width - 40)

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



        pygame.display.flip()
