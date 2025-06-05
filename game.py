import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player1 = pygame.image.load('barco/barco1.png').convert_alpha()
        player2 = pygame.image.load('barco/barco2.png').convert_alpha()
        player3 = pygame.image.load('barco/barco3.png').convert_alpha()
        player4 = pygame.image.load('barco/barco4.png').convert_alpha()
        player5 = pygame.image.load('barco/barco5.png').convert_alpha()
        player6 = pygame.image.load('barco/barco6.png').convert_alpha()
        player7 = pygame.image.load('barco/barco7.png').convert_alpha()
        player8 = pygame.image.load('barco/barco8.png').convert_alpha()
        player9 = pygame.image.load('barco/barco9.png').convert_alpha()
        
        self.frames = [player1, player2, player3, player4, player5, player6, player7, player8, player9]
        self.player_index = 0


        self.image = self.frames[self.player_index]
        self.rect = self.image.get_rect(midbottom=(largura/2, 400))


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.player_index -= 0.1
            if self.player_index < 0:
                self.player_index = 8
            self.image = self.frames[int(self.player_index)]

            self.rect.x -= 3
        elif keys[pygame.K_RIGHT] and self.rect.right <= largura:
            self.player_index += 0.1
            if self.player_index >= 9:
                self.player_index = 0
            self.image = self.frames[int(self.player_index)]

            self.rect.x += 3
        else:
            self.player_index = int(self.player_index)
        



    def animation(self):
        self.player_index += 0.1
        if self.player_index >= len(self.frames): self.player_index = 0
        self.image = self.frames[int(self.player_index)]


    def update(self):
        self.player_input()



pygame.init()

largura = 800
altura = 400
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Catch The Coin")

clock = pygame.time.Clock()

#Grupos
player = pygame.sprite.GroupSingle()
player.add(Player())










while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('white')
    
    player.draw(screen)
    player.update()




    pygame.display.update()
    clock.tick(60)