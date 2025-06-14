"""import pygame, sys
from tkinter import Button

from matplotlib.font_manager import get_font

pygame.init()


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)

        if self.image is None:
            self.image = self.next

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, menu):
        if self.image is None:
            menu.blit(self.image, self.rect)
        menu.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[o] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


menu = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("MENU")

menubg = pygame.image.load("fundo/fundo7.png").convert()

def main_menu(): #main menu tela
    pygame.display.set_caption("MENU")

    while True:
        menu.blit(menu, (0,0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(500, 300))

        play_button = Button(image=pygame.image.load("play.jpg"), pos= (500, 400), text_input= "play", font= get_font(75), base_color= "#d7fcd4", hovering_color= "white")

        option_button = Button(image=pygame.image.load("option.jpg"), pos=(500, 300), text_input="options", font=get_font(75), base_color="#d7fcd4", hovering_color="white")

        quit_button = Button(image=pygame.image.load("quit.jpg"), pos=(500, 400), text_input="quit", font=get_font(75), base_color="#d7fcd4", hovering_color="white")

        menu.blit(menu_text, menu_rect)

        for button in [play_button, option_button, play_button]:
            button.changecolor(menu_mouse_pos)
            button.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()

                if option_button.checkForInput(menu_mouse_pos):
                    options()

                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def play(): #Play menu
    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        menu.fill("black")

        play_text = get_font(45).render("This is the PLAY screen", True, "White")
        play_rect = play_text.get_rect(center=(500, 400))
        menu.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(500, 500), text_input="Back", font=get_font(75), base_color="White", hovering_color="Grenn")
        play_back.changeColor(play_mouse_pos)
        play_back.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(pygame.mouse):
                    main_menu()

        pygame.display.update()

def options(): #Options menu
    options_mouse_pos = pygame.mouse.get_pos()

    menu.fill("black")

    options_text = get_font(45).render("This is the OPTIONS screen", True, "Black")
    options_rect = options_text.get_rect(center=(500, 300))
    menu.blit(options_text, options_rect)

    options_back = Button(image= None, pos= (500, 360), text_input= "back", font=get_font(75), base_color="Black", hovering_color="Grenn")
    options_back.changeColor(options_mouse_pos)
    options_back.update(menu)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if options_back.checkForInput(pygame.mouse):
                main_menu()

    pygame.display.update()


main_menu()
"""

import pygame
import sys
import config
pygame.init()

# Função para carregar fontes do sistema
def get_font(size):
    return pygame.font.SysFont("Arial", size)

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



"""
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image if image is not None else pygame.Surface((250, 75), pygame.SRCALPHA)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
"""
# Tela principal
menu = pygame.display.set_mode((config.largura, config.altura))
pygame.display.set_caption("MENU")
menubg = pygame.Surface((config.largura, config.altura))
menubg = pygame.image.load("graficos/fundo/fundo7.png").convert()
"""def main_menu():
    from game import play
    while True:
        menu.blit(menubg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = get_font(80).render("MAIN MENU", True, "#b68f40")
        title_rect = title_text.get_rect(center=(500, 100))
        menu.blit(title_text, title_rect)

        play_button = Button(None, (500, 300), "Play", get_font(50), "#d7fcd4", "green")
        options_button = Button(None, (500, 400), "Options", get_font(50), "#d7fcd4", "green")
        quit_button = Button(None, (500, 500), "Quit", get_font(50), "#d7fcd4", "green")

        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    play()
                if options_button.checkForInput(mouse_pos):
                    options()
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()"""

"""def play():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        menu.fill("black")

        text = get_font(40).render("This is the PLAY screen", True, "white")
        rect = text.get_rect(center=(500, 350))
        menu.blit(text, rect)

        back_button = Button(None, (500, 450), "Back", get_font(50), "white", "green")
        back_button.changeColor(mouse_pos)
        back_button.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    return

        pygame.display.update()"""

def options():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        menu.fill("black")

        text = get_font(40).render("This is the OPTIONS screen", True, "white")
        rect = text.get_rect(center=(500, 350))
        menu.blit(text, rect)

        back_button = Button(None, (500, 450), "Back", get_font(50), "white", "green")
        back_button.changeColor(mouse_pos)
        back_button.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    return

        pygame.display.update()

# Iniciar o menu
#main_menu()

"""import pygame, sys
from tkinter import Button

from matplotlib.font_manager import get_font

pygame.init()


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)

        if self.image is None:
            self.image = self.next

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, menu):
        if self.image is None:
            menu.blit(self.image, self.rect)
        menu.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[o] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


menu = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("MENU")

menubg = pygame.image.load("fundo/fundo7.png").convert()

def main_menu(): #main menu tela
    pygame.display.set_caption("MENU")

    while True:
        menu.blit(menu, (0,0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(500, 300))

        play_button = Button(image=pygame.image.load("play.jpg"), pos= (500, 400), text_input= "play", font= get_font(75), base_color= "#d7fcd4", hovering_color= "white")

        option_button = Button(image=pygame.image.load("option.jpg"), pos=(500, 300), text_input="options", font=get_font(75), base_color="#d7fcd4", hovering_color="white")

        quit_button = Button(image=pygame.image.load("quit.jpg"), pos=(500, 400), text_input="quit", font=get_font(75), base_color="#d7fcd4", hovering_color="white")

        menu.blit(menu_text, menu_rect)

        for button in [play_button, option_button, play_button]:
            button.changecolor(menu_mouse_pos)
            button.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()

                if option_button.checkForInput(menu_mouse_pos):
                    options()

                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def play(): #Play menu
    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        menu.fill("black")

        play_text = get_font(45).render("This is the PLAY screen", True, "White")
        play_rect = play_text.get_rect(center=(500, 400))
        menu.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(500, 500), text_input="Back", font=get_font(75), base_color="White", hovering_color="Grenn")
        play_back.changeColor(play_mouse_pos)
        play_back.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(pygame.mouse):
                    main_menu()

        pygame.display.update()

def options(): #Options menu
    options_mouse_pos = pygame.mouse.get_pos()

    menu.fill("black")

    options_text = get_font(45).render("This is the OPTIONS screen", True, "Black")
    options_rect = options_text.get_rect(center=(500, 300))
    menu.blit(options_text, options_rect)

    options_back = Button(image= None, pos= (500, 360), text_input= "back", font=get_font(75), base_color="Black", hovering_color="Grenn")
    options_back.changeColor(options_mouse_pos)
    options_back.update(menu)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if options_back.checkForInput(pygame.mouse):
                main_menu()

    pygame.display.update()


main_menu()
"""

import pygame
import sys
import config
pygame.init()

# Função para carregar fontes do sistema
def get_font(size):
    return pygame.font.SysFont("Arial", size)

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



"""
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image if image is not None else pygame.Surface((250, 75), pygame.SRCALPHA)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
"""
# Tela principal
over = pygame.display.set_mode((config.largura, config.altura))
pygame.display.set_caption("GAME OVER")
overbg = pygame.Surface((config.largura, config.altura))
overbg = pygame.image.load("graficos/fundo/fundogameover.png").convert()
"""def main_menu():
    from game import play
    while True:
        menu.blit(menubg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        title_text = get_font(80).render("MAIN MENU", True, "#b68f40")
        title_rect = title_text.get_rect(center=(500, 100))
        menu.blit(title_text, title_rect)

        play_button = Button(None, (500, 300), "Play", get_font(50), "#d7fcd4", "green")
        options_button = Button(None, (500, 400), "Options", get_font(50), "#d7fcd4", "green")
        quit_button = Button(None, (500, 500), "Quit", get_font(50), "#d7fcd4", "green")

        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    play()
                if options_button.checkForInput(mouse_pos):
                    options()
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()"""

"""def play():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        menu.fill("black")

        text = get_font(40).render("This is the PLAY screen", True, "white")
        rect = text.get_rect(center=(500, 350))
        menu.blit(text, rect)

        back_button = Button(None, (500, 450), "Back", get_font(50), "white", "green")
        back_button.changeColor(mouse_pos)
        back_button.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    return

        pygame.display.update()"""

def options():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        menu.fill("black")

        text = get_font(40).render("This is the OPTIONS screen", True, "white")
        rect = text.get_rect(center=(500, 350))
        menu.blit(text, rect)

        back_button = Button(None, (500, 450), "Back", get_font(50), "white", "green")
        back_button.changeColor(mouse_pos)
        back_button.update(menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    return

        pygame.display.update()

# Iniciar o menu
#main_menu()
