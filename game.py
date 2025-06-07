import pygame
from sys import exit
from random import randint, choice

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

        self.peso = 0
        self.pontuacao = 0
        self.pontos = 0
        self.velocidade = 0
        self.vidaAtual = 3

        self.image = self.frames[self.player_index]
        self.rect = self.image.get_rect(midbottom=(largura/2, altura))


    def player_input(self):
        keys = pygame.key.get_pressed()
        self.velocidade = 10 - self.peso

        lentidao_animacao = int(self.peso) / 100





        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            pass
        else:
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right <= largura:
                self.player_index += 0.15 - lentidao_animacao
                if self.player_index >= 9:
                    self.player_index = 0
                self.image = self.frames[int(self.player_index)]

                self.rect.x += self.velocidade
            elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left >= 0:
                self.player_index -= 0.15 - lentidao_animacao
                if self.player_index < 0:
                    self.player_index = 8
                self.image = self.frames[int(self.player_index)]

                self.rect.x -= self.velocidade
        
            else:
                self.player_index = int(self.player_index)
        

    def mostrarVida(self):
        coracaoCheio = pygame.image.load('coracao/coracaoCheio.png')
        coracaoVazio = pygame.image.load('coracao/coracaoVazio.png')

        coracaoCheio = pygame.transform.scale(coracaoCheio, (45,50))
        coracaoVazio = pygame.transform.scale(coracaoVazio, (45,50))


        


        pos_x_coracao = 5
        if self.vidaAtual == 3:
            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            screen.blit(coracaoCheio, coracaoCheio_rect)

            pos_x_coracao += 45 + 8
            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            screen.blit(coracaoCheio, coracaoCheio_rect)
            pos_x_coracao += 45 + 8

            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            screen.blit(coracaoCheio, coracaoCheio_rect)
        elif self.vidaAtual == 2:
            pos_x_coracao = 0
            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            screen.blit(coracaoCheio, coracaoCheio_rect)
            pos_x_coracao += 45 + 8

            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            screen.blit(coracaoCheio, coracaoCheio_rect)

            pos_x_coracao += 45 + 8

            coracaoVazio_rect = coracaoVazio.get_rect(topleft=(pos_x_coracao,7))
            screen.blit(coracaoVazio, coracaoVazio_rect)
        elif self.vidaAtual == 1:
            pos_x_coracao = 0
            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            screen.blit(coracaoCheio, coracaoCheio_rect)
            pos_x_coracao += 45 + 8

            coracaoVazio_rect = coracaoVazio.get_rect(topleft=(pos_x_coracao,7))
            screen.blit(coracaoVazio, coracaoVazio_rect)

            pos_x_coracao += 45 + 8

            coracaoVazio_rect = coracaoVazio.get_rect(topleft=(pos_x_coracao,7))
            screen.blit(coracaoVazio, coracaoVazio_rect)









    def colisaoMoeda(self):

        if self.peso < 8:

            moeda_colidida = pygame.sprite.spritecollide(player.sprite, moeda_group, True)
            for moeda in moeda_colidida:
                if moeda.tipo == 'ouro':
                    self.peso += 0.5
                    self.pontos += 3

                if moeda.tipo == 'prata':
                    self.peso += 0.3
                    self.pontos += 2


                if moeda.tipo == 'bronze':
                    self.peso += 0.1
                    self.pontos += 1
        
    def colisaoBomba(self):
        if pygame.sprite.spritecollide(player.sprite, inimigo_group, True):
            self.vidaAtual -= 1

        if self.vidaAtual <= 0:
            pygame.quit()
            exit()


    def colisaoPowerUp(self):
        
        power_up_colidido = pygame.sprite.spritecollide(player.sprite, powerup_group, True)

        for powerUp in power_up_colidido:
            if powerUp.tipo == 'vida':
                if self.vidaAtual < 3:
                    self.vidaAtual += 1





    def update(self):
        self.player_input()
        self.colisaoMoeda()
        self.colisaoBomba()
        self.colisaoPowerUp()
        self.mostrarVida()





class Moeda(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()

        if tipo == 'ouro':
            ouro_1 = pygame.image.load('moeda/ouro/moedaouro1.png').convert_alpha()
            ouro_2 = pygame.image.load('moeda/ouro/moedaouro2.png').convert_alpha()
            ouro_3 = pygame.image.load('moeda/ouro/moedaouro3.png').convert_alpha()
            ouro_4 = pygame.image.load('moeda/ouro/moedaouro4.png').convert_alpha()
            ouro_5 = pygame.image.load('moeda/ouro/moedaouro5.png').convert_alpha()
            ouro_6 = pygame.image.load('moeda/ouro/moedaouro6.png').convert_alpha()
            ouro_7 = pygame.image.load('moeda/ouro/moedaouro7.png').convert_alpha()
            ouro_8 = pygame.image.load('moeda/ouro/moedaouro8.png').convert_alpha()
            
            self.frames = [ouro_1, ouro_2, ouro_3, ouro_4, ouro_5, ouro_6, ouro_7, ouro_8]
            self.gravidade = randint(5, 7)
            self.tipo = 'ouro'
        elif tipo == 'prata':
            prata_1 = pygame.image.load('moeda/prata/moedaprata1.png').convert_alpha()
            prata_2 = pygame.image.load('moeda/prata/moedaprata2.png').convert_alpha()
            prata_3 = pygame.image.load('moeda/prata/moedaprata3.png').convert_alpha()
            prata_4 = pygame.image.load('moeda/prata/moedaprata4.png').convert_alpha()
            prata_5 = pygame.image.load('moeda/prata/moedaprata5.png').convert_alpha()
            prata_6 = pygame.image.load('moeda/prata/moedaprata6.png').convert_alpha()
            prata_7 = pygame.image.load('moeda/prata/moedaprata7.png').convert_alpha()
            prata_8 = pygame.image.load('moeda/prata/moedaprata8.png').convert_alpha()
            self.frames = [prata_1, prata_2, prata_3, prata_4, prata_5, prata_6, prata_7, prata_8]
            self.gravidade = randint(3, 5)
            self.tipo = 'prata'

        elif tipo == 'bronze':
            bronze_1 = pygame.image.load('moeda/bronze/moedabronze1.png').convert_alpha()
            bronze_2 = pygame.image.load('moeda/bronze/moedabronze2.png').convert_alpha()
            bronze_3 = pygame.image.load('moeda/bronze/moedabronze3.png').convert_alpha()
            bronze_4 = pygame.image.load('moeda/bronze/moedabronze4.png').convert_alpha()
            bronze_5 = pygame.image.load('moeda/bronze/moedabronze5.png').convert_alpha()
            bronze_6 = pygame.image.load('moeda/bronze/moedabronze6.png').convert_alpha()
            bronze_7 = pygame.image.load('moeda/bronze/moedabronze7.png').convert_alpha()
            bronze_8 = pygame.image.load('moeda/bronze/moedabronze8.png').convert_alpha()
            self.frames = [bronze_1, bronze_2, bronze_3, bronze_4, bronze_5, bronze_6, bronze_7, bronze_8]
            self.gravidade = randint(2, 4)
            self.tipo = 'bronze'

        self.animacao_index = 0
        self.image = self.frames[self.animacao_index]
        self.rect = self.image.get_rect(midbottom=(randint(9, largura-9), randint(-100, 0))) # Pode colocar um numero aleatorio para randomizar a queda das moedas




    def queda(self):
        self.rect.y += self.gravidade


    def destruir(self):
        if self.rect.y >= altura + 50:
            self.kill()



    def animacao(self):
        self.animacao_index += 0.1
        if self.animacao_index >= len(self.frames): self.animacao_index = 0
        self.image = self.frames[int(self.animacao_index)]

    def update(self):
        self.animacao()
        self.queda()
        self.destruir()


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()

        self.tipo = tipo

        if tipo == 'bomba':
            bomb_1 = pygame.image.load('bomba/bomb1.png').convert_alpha()
            bomb_2 = pygame.image.load('bomba/bomb2.png').convert_alpha()
            bomb_3 = pygame.image.load('bomba/bomb3.png').convert_alpha()
            bomb_4 = pygame.image.load('bomba/bomb4.png').convert_alpha()
            bomb_5 = pygame.image.load('bomba/bomb5.png').convert_alpha()
            bomb_6 = pygame.image.load('bomba/bomb6.png').convert_alpha()

            self.frames = [bomb_1, bomb_2, bomb_3, bomb_4, bomb_5, bomb_6]

            self.bomb_index = 0

            self.image = self.frames[self.bomb_index]

            inicio = randint(-100, 0)
            inicioPositivo = inicio * -1
            distanciaApercorrer = inicioPositivo + altura - 250
            self.distanciaDeTroca = distanciaApercorrer // 6
            self.rect = self.image.get_rect(midbottom=((randint(9, largura-9), inicio)))
            self.gravidade = randint(1, 12)

        elif tipo == 'flecha':
            flecha_1 = pygame.image.load('flecha/flecha1.png')
            flecha_2 = pygame.image.load('flecha/flecha2.png')
            flecha_3 = pygame.image.load('flecha/flecha3.png')
            flecha_4 = pygame.image.load('flecha/flecha4.png')
            
            flecha_1 = pygame.transform.scale2x(flecha_1)
            flecha_2 = pygame.transform.scale2x(flecha_2)
            flecha_3 = pygame.transform.scale2x(flecha_3)
            flecha_4 = pygame.transform.scale2x(flecha_4)


            self.frames = [flecha_1,flecha_2,flecha_3,flecha_4]


            self.flecha_index = 0
            self.image = self.frames[self.flecha_index]

            inicio = randint(-100, 0)
            self.rect = self.image.get_rect(midbottom=((randint(9, largura-9), inicio)))
            self.gravidade = randint(1, 4)
            self.velocidadeFlecha = choice([0.1, 0.2, 0.3, 0.4, 0.5])


    def queda(self):
        if self.tipo == 'flecha':
            self.gravidade += self.velocidadeFlecha
            self.rect.y += self.gravidade
        if self.tipo == 'bomba':
            self.rect.y += self.gravidade

    def destruir(self):
        if self.rect.y >= altura + 50:
            self.kill()



    def animacao(self):
        if self.tipo == 'bomba' and self.rect.y >= self.distanciaDeTroca:
            self.bomb_index += 1
            self.distanciaDeTroca += self.distanciaDeTroca
            self.image = self.frames[int(self.bomb_index)]

        if self.tipo == 'flecha':
            self.flecha_index += 0.1
            if self.flecha_index >= len(self.frames): self.flecha_index = 0
            self.image = self.frames[int(self.flecha_index)]



    def update(self):
        self.animacao()
        self.queda()
        self.destruir()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()

        self.tipo = tipo

        if tipo == 'vida':
            vida_1 = pygame.image.load('powerups/vida/vida1.png')
            vida_2 = pygame.image.load('powerups/vida/vida2.png')
            vida_3 = pygame.image.load('powerups/vida/vida3.png')
            vida_4 = pygame.image.load('powerups/vida/vida4.png')
            vida_5 = pygame.image.load('powerups/vida/vida5.png')
            vida_6 = pygame.image.load('powerups/vida/vida6.png')
            vida_7 = pygame.image.load('powerups/vida/vida7.png')
            vida_8 = pygame.image.load('powerups/vida/vida8.png')
            vida_9 = pygame.image.load('powerups/vida/vida9.png')
            vida_10 = pygame.image.load('powerups/vida/vida10.png')
            vida_11 = pygame.image.load('powerups/vida/vida11.png')
            vida_12 = pygame.image.load('powerups/vida/vida12.png')

            vida_1 = pygame.transform.scale2x(vida_1)
            vida_2 = pygame.transform.scale2x(vida_2)
            vida_3 = pygame.transform.scale2x(vida_3)
            vida_4 = pygame.transform.scale2x(vida_4)
            vida_5 = pygame.transform.scale2x(vida_5)
            vida_6 = pygame.transform.scale2x(vida_6)
            vida_7 = pygame.transform.scale2x(vida_7)
            vida_8 = pygame.transform.scale2x(vida_8)
            vida_9 = pygame.transform.scale2x(vida_9)
            vida_10 = pygame.transform.scale2x(vida_10)
            vida_11 = pygame.transform.scale2x(vida_11)
            vida_12 = pygame.transform.scale2x(vida_12)







            self.frames = [vida_1,vida_2,vida_3,vida_4,vida_5,vida_6,vida_7,vida_8,vida_9,vida_10,vida_11,vida_12]

            self.gravidade = randint(1, 12)

            self.powerup_index = 0

            self.image = self.frames[self.powerup_index]
            self.rect = self.image.get_rect(midbottom=(randint(9, largura-9), randint(-100, -1)))


    def queda(self):
        self.rect.y += self.gravidade

    def animacao(self):
        self.powerup_index += 0.1
        if self.powerup_index >= len(self.frames): self.powerup_index = 0
        self.image = self.frames[int(self.powerup_index)]

    def destruir(self):
        if self.rect.y >= altura + 50:
            self.kill()


    def update(self):
        self.animacao()
        self.queda()
        self.destruir


pygame.init()
test_font = pygame.font.Font('fonte/Pixeltype.ttf', 50)
mensagem_test_font = pygame.font.Font('fonte/Pixeltype.ttf', 15)

largura = 1000
altura = 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Catch The Coin")


clock = pygame.time.Clock()

#Grupos
player = pygame.sprite.GroupSingle()
player.add(Player())

moeda_group = pygame.sprite.Group()

inimigo_group = pygame.sprite.Group()

powerup_group = pygame.sprite.Group()


tempo_colisao_Porto = 0


    



# Timers

moeda_timer = pygame.USEREVENT + 1
pygame.time.set_timer(moeda_timer, 400)

inimigo_timer = pygame.USEREVENT + 2
pygame.time.set_timer(inimigo_timer, 1000)

powerup_timer = pygame.USEREVENT + 3
pygame.time.set_timer(powerup_timer, 5000)




tempo_total = 2 * 60  
tempo_inicio = pygame.time.get_ticks()

def verificar_timer(cor_score):
    tempo_decorrido = (pygame.time.get_ticks() - tempo_inicio) // 1000
    tempo_restante = max(0, tempo_total - tempo_decorrido)  # Impede valores negativos

    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    minutos = int(minutos)
    segundos = int(segundos)

    timer_surf = test_font.render(f'{minutos:02}:{segundos:02}', False, cor_score)
    timer_rect = timer_surf.get_rect(midtop=(largura/2, 20))
    screen.blit(timer_surf, timer_rect)

    if tempo_restante == 0:
        pygame.quit() # Melhorar a lógica de parada por tempo
        exit()


score = 0



def escolher_fundo(fundoSorteado):
    cor_score = ()
    if fundoSorteado == 1:
        fundo_surf = pygame.image.load('fundo/fundo1.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (largura, altura))

        cor_score =  (64,64,64)
    if fundoSorteado == 2:
        fundo_surf = pygame.image.load('fundo/fundo2.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (largura, altura))

        cor_score =  (64,64,64)


    if fundoSorteado == 3:
        fundo_surf = pygame.image.load('fundo/fundo3.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (largura, altura))

        cor_score =  'white'

    if fundoSorteado == 4:
        fundo_surf = pygame.image.load('fundo/fundo4.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (largura, altura)) 

        cor_score =  (64,64,64)


    if fundoSorteado == 5:
        fundo_surf = pygame.image.load('fundo/fundo5.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (largura, altura)) 

        cor_score =  (64,64,64)


    if fundoSorteado == 6:
        fundo_surf = pygame.image.load('fundo/fundo6.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (largura, altura))  

        cor_score =  'white'


    if fundoSorteado == 7:
        fundo_surf = pygame.image.load('fundo/fundo7.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (largura, altura))

        cor_score =  (64,64,64)


    return fundo_surf, cor_score

def mostrar_fundo(fundo):

    screen.blit(fundo, (0, 0))

cont_fundo = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        if event.type == moeda_timer:
            moeda_group.add(Moeda(choice(['ouro', 'prata', 'prata', 'bronze', 'bronze', 'bronze'])))

        if event.type == inimigo_timer:
            inimigo_group.add(Inimigo(choice(['bomba','flecha'])))

        if event.type == powerup_timer:
            powerup_group.add(PowerUp('vida'))




    if cont_fundo == 0:
        cont_fundo = 1
        if cont_fundo == 1:
            fundoSorteado = randint(1, 7)
            fundo_surf, cor_score = escolher_fundo(fundoSorteado)

    mostrar_fundo(fundo_surf)



    score_text = test_font.render(f'Score: {score}', False, cor_score)
    score_text_rect = score_text.get_rect(topright=(largura-20, 20))
    screen.blit(score_text,score_text_rect)

    mensagem_text = mensagem_test_font.render('Barco cheio. Descarregue no porto', False, cor_score)
    mensagem_text_rect = mensagem_text.get_rect(midbottom=(player.sprite.rect.x + 55, altura-50))
    



    porto_surf = pygame.image.load('porto/porto.png')
    porto_rect = porto_surf.get_rect(bottomright=(largura, altura+38))

    screen.blit(porto_surf, porto_rect)


    
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

            timer_Porto = test_font.render(f'{int(tempo_restante // 1000 + 1)}', False, cor_score)
            timer_Porto_rect = score_text.get_rect(bottomright=(largura, altura-80))
            screen.blit(timer_Porto,timer_Porto_rect)

        
    else:
        tempo_colisao_Porto = 0          



    if player.sprite.peso >= 8:
        screen.blit(mensagem_text,mensagem_text_rect)






    moeda_group.draw(screen)
    moeda_group.update()

    inimigo_group.draw(screen)
    inimigo_group.update()

    powerup_group.draw(screen)
    powerup_group.update()


    player.draw(screen)
    player.update()



    pygame.display.update()
    clock.tick(60)