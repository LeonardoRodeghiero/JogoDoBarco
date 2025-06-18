import pygame
import sys
import config
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
overbg = pygame.image.load("graficos/fundo/fundogameover.png").convert()
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
    one_p_button = Button(one_p_default, one_p_hover, (config.largura/2, 170), "", get_font(50), "#d7fcd4", "green")

    two_p_default = pygame.transform.scale(pygame.image.load('graficos/botoes/2playerswhite.png').convert_alpha(), (150, 60))
    two_p_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/2playersgreen.png').convert_alpha(), (150, 60))
    two_p_button = Button(two_p_default, two_p_hover, (config.largura/2, 170), "", get_font(50), "#d7fcd4", "green")
    botao_ativo = one_p_button

    back_default = pygame.transform.scale(pygame.image.load('graficos/botoes/backwhite.png').convert_alpha(), (150, 60))
    back_hover = pygame.transform.scale(pygame.image.load('graficos/botoes/backgreen.png').convert_alpha(), (150, 60))
    back_button = Button(back_default, back_hover, (config.largura/2, 500), "", get_font(50), "#d7fcd4", "green")

    while True:
        menu.blit(menubg, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        title_text = config.title_font.render("SELECIONE O MODO", True, "#b68f40")
        title_rect = title_text.get_rect(center=(config.largura/2, 100))
        menu.blit(title_text, title_rect)
        
        for button in [botao_ativo, back_button]:
            button.changeColor(mouse_pos)
            button.update(menu)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_ativo.checkForInput(mouse_pos):
                    if botao_ativo == one_p_button:
                        botao_ativo = two_p_button
                        config.modo_jogo = 2
                    else:
                        botao_ativo = one_p_button
                        config.modo_jogo = 1
                if back_button.checkForInput(mouse_pos):
                    return "menu"

        pygame.display.update()


