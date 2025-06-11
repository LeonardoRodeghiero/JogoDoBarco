import pygame
import config


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player1 = pygame.image.load('graficos/barco/barco1.png').convert_alpha()
        player2 = pygame.image.load('graficos/barco/barco2.png').convert_alpha()
        player3 = pygame.image.load('graficos/barco/barco3.png').convert_alpha()
        player4 = pygame.image.load('graficos/barco/barco4.png').convert_alpha()
        player5 = pygame.image.load('graficos/barco/barco5.png').convert_alpha()
        player6 = pygame.image.load('graficos/barco/barco6.png').convert_alpha()
        player7 = pygame.image.load('graficos/barco/barco7.png').convert_alpha()
        player8 = pygame.image.load('graficos/barco/barco8.png').convert_alpha()
        player9 = pygame.image.load('graficos/barco/barco9.png').convert_alpha()
        
        self.frames = [player1, player2, player3, player4, player5, player6, player7, player8, player9]
        self.player_index = 0

        self.peso = 0
        self.pontuacao = 0
        self.pontos = 0
        self.velocidadeNormal = 10
        self.velocidade = self.velocidadeNormal
        self.vidaAtual = 3
        self.PowerUpsAtivos = []


        #Atributos PowerUps de velocidade
        self.powerUp_velocidade_ativo = False
        self.tempo_inicioPowerUpVelocidade = None
        self.tempoTotalPowerUpVelocidade = 15000


        #Atributos PowerUps de Teste
        self.powerUp_Teste_ativo = False
        self.tempo_inicioPowerUpTeste = None
        self.tempoTotalPowerUpTeste = 15000

        #Atributos PowerUps de moeda x2
        self.powerUp_moeda2x_ativo = False
        self.tempo_inicioPowerUpMoeda2x = None
        self.tempoTotalPowerUpMoeda2x = 15000
        self.multMoeda2x = 1

        



        self.image = self.frames[self.player_index]
        self.rect = self.image.get_rect(midbottom=(config.largura/2, config.altura))


    def player_input(self):
        keys = pygame.key.get_pressed()

        lentidao_animacao = int(self.peso) / 100





        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            pass
        else:
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right <= config.largura:
                self.player_index += 0.15 - lentidao_animacao
                if self.player_index >= 9:
                    self.player_index = 0
                self.image = self.frames[int(self.player_index)]

                self.rect.x += self.velocidade - self.peso
            elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left >= 0:
                self.player_index -= 0.15 - lentidao_animacao
                if self.player_index < 0:
                    self.player_index = 8
                self.image = self.frames[int(self.player_index)]

                self.rect.x -= self.velocidade - self.peso
        
            else:
                self.player_index = int(self.player_index)
        

    def mostrarVida(self):
        coracaoCheio = pygame.image.load('graficos/coracao/coracaoCheio.png')
        coracaoVazio = pygame.image.load('graficos/coracao/coracaoVazio.png')

        coracaoCheio = pygame.transform.scale(coracaoCheio, (45,50))
        coracaoVazio = pygame.transform.scale(coracaoVazio, (45,50))


        


        pos_x_coracao = 5
        if self.vidaAtual == 3:
            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            config.screen.blit(coracaoCheio, coracaoCheio_rect)

            pos_x_coracao += 45 + 8
            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            config.screen.blit(coracaoCheio, coracaoCheio_rect)
            pos_x_coracao += 45 + 8

            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            config.screen.blit(coracaoCheio, coracaoCheio_rect)
        elif self.vidaAtual == 2:
            pos_x_coracao = 0
            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            config.screen.blit(coracaoCheio, coracaoCheio_rect)
            pos_x_coracao += 45 + 8

            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            config.screen.blit(coracaoCheio, coracaoCheio_rect)

            pos_x_coracao += 45 + 8

            coracaoVazio_rect = coracaoVazio.get_rect(topleft=(pos_x_coracao,7))
            config.screen.blit(coracaoVazio, coracaoVazio_rect)
        elif self.vidaAtual == 1:
            pos_x_coracao = 0
            coracaoCheio_rect = coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
            config.screen.blit(coracaoCheio, coracaoCheio_rect)
            pos_x_coracao += 45 + 8

            coracaoVazio_rect = coracaoVazio.get_rect(topleft=(pos_x_coracao,7))
            config.screen.blit(coracaoVazio, coracaoVazio_rect)

            pos_x_coracao += 45 + 8

            coracaoVazio_rect = coracaoVazio.get_rect(topleft=(pos_x_coracao,7))
            config.screen.blit(coracaoVazio, coracaoVazio_rect)









    def colisaoMoeda(self):

        if self.peso < 8:

            moeda_colidida = pygame.sprite.spritecollide(player.sprite, config.moeda_group, True)
            for moeda in moeda_colidida:
                if moeda.tipo == 'ouro':
                    self.peso += 0.5
                    self.pontos += 3 * self.multMoeda2x

                if moeda.tipo == 'prata':
                    self.peso += 0.3
                    self.pontos += 2 * self.multMoeda2x


                if moeda.tipo == 'bronze':
                    self.peso += 0.1
                    self.pontos += 1 * self.multMoeda2x
        
    def colisaoBomba(self):
        if pygame.sprite.spritecollide(player.sprite, config.inimigo_group, True):
            self.vidaAtual -= 1

        if self.vidaAtual <= 0:
            pygame.quit()
            exit()


    def colisaoPowerUp(self):
        from tempo import adicionarTempo

        power_up_colidido = pygame.sprite.spritecollide(player.sprite, config.powerup_group, True)

        for powerUp in power_up_colidido:
            if powerUp.tipo == 'vida':
                if self.vidaAtual < 3:
                    self.vidaAtual += 1
            if powerUp.tipo == 'velocidade':
                self.ativar_power_up('velocidade')

            """if powerUp.tipo == 'vida':
                self.ativar_power_up('teste')
            """
            if powerUp.tipo == 'moeda2x':
                self.ativar_power_up('moeda2x')

            if powerUp.tipo == 'tempo':
                adicionarTempo(10)


    def ativar_power_up(self, powerUpTipo):
        """Ativa a habilidade temporária"""
        if powerUpTipo == 'velocidade':
            if self.powerUp_velocidade_ativo == False:
                self.PowerUpsAtivos.append(['velocidade', 'yellow', 0])

            self.powerUp_velocidade_ativo = True
            self.tempo_inicioPowerUpVelocidade = pygame.time.get_ticks()  # Guarda o tempo inicial

        if powerUpTipo =='teste':
            if self.powerUp_Teste_ativo == False:
                self.PowerUpsAtivos.append(['teste', 'green', 0])

            self.powerUp_Teste_ativo = True
            self.tempo_inicioPowerUpTeste = pygame.time.get_ticks()  # Guarda o tempo inicial


        if powerUpTipo == 'moeda2x':
            if self.powerUp_moeda2x_ativo == False:
                self.PowerUpsAtivos.append(['moeda2x', 'orange', 0])
            
            self.powerUp_moeda2x_ativo = True
            self.tempo_inicioPowerUpMoeda2x = pygame.time.get_ticks()



    def poderPowerUp(self):

        for powerUp in self.PowerUpsAtivos:
            if powerUp[0] == 'velocidade':
                self.velocidade = self.velocidadeNormal + 10

            if powerUp[0] == 'moeda2x':
                self.multMoeda2x = 2


        if self.powerUp_velocidade_ativo == False:
            self.velocidade = self.velocidadeNormal

        if self.powerUp_moeda2x_ativo == False:
            self.multMoeda2x = 1

    def verificar_tempo(self):
        """Verifica se os 15 segundos já passaram"""
        if self.powerUp_velocidade_ativo and self.tempo_inicioPowerUpVelocidade:
            tempo_decorrido_velocidade = pygame.time.get_ticks() - self.tempo_inicioPowerUpVelocidade
            if tempo_decorrido_velocidade >= self.tempoTotalPowerUpVelocidade:  # 15 segundos em milissegundos
                self.powerUp_velocidade_ativo = False  # Desativa a habilidade
                
                self.PowerUpsAtivos = [p for p in self.PowerUpsAtivos if p[0] != "velocidade"]


        if self.powerUp_Teste_ativo and self.tempo_inicioPowerUpTeste:
            tempo_decorrido_teste = pygame.time.get_ticks() - self.tempo_inicioPowerUpTeste
            if tempo_decorrido_teste >= self.tempoTotalPowerUpTeste:  # 15 segundos em milissegundos
                self.powerUp_Teste_ativo = False  # Desativa a habilidade
                self.PowerUpsAtivos = [p for p in self.PowerUpsAtivos if p[0] != "teste"]
    

        if self.powerUp_moeda2x_ativo and self.tempo_inicioPowerUpMoeda2x:
            tempo_decorrido_moeda2x = pygame.time.get_ticks() - self.tempo_inicioPowerUpMoeda2x
            if tempo_decorrido_moeda2x >= self.tempoTotalPowerUpMoeda2x:  # 15 segundos em milissegundos
                self.powerUp_moeda2x_ativo = False  # Desativa a habilidade
                self.PowerUpsAtivos = [p for p in self.PowerUpsAtivos if p[0] != "moeda2x"]
    


    def tempo_restante(self):
        """Retorna o tempo restante"""
        if self.powerUp_velocidade_ativo and self.tempo_inicioPowerUpVelocidade:
            tempo_decorrido_velocidade = (pygame.time.get_ticks() - self.tempo_inicioPowerUpVelocidade) // 1000
            tempo_restante_velocidade = max(0, self.tempoTotalPowerUpVelocidade // 1000 - tempo_decorrido_velocidade)


            for powerUp in self.PowerUpsAtivos:
                if powerUp[0] == 'velocidade':
                    segundos_velocidade = int(tempo_restante_velocidade % 60)
                    powerUp[2] = segundos_velocidade

        if self.powerUp_Teste_ativo and self.tempo_inicioPowerUpTeste:
            tempo_decorrido_teste = (pygame.time.get_ticks() - self.tempo_inicioPowerUpTeste) // 1000
            tempo_restante_teste = max(0, self.tempoTotalPowerUpTeste // 1000 - tempo_decorrido_teste)


            for powerUp in self.PowerUpsAtivos:
                if powerUp[0] == 'teste':
                    segundos_teste = int(tempo_restante_teste % 60)
                    powerUp[2] = segundos_teste

        if self.powerUp_moeda2x_ativo and self.tempo_inicioPowerUpMoeda2x:
            tempo_decorrido_moeda2x = (pygame.time.get_ticks() - self.tempo_inicioPowerUpMoeda2x) // 1000
            tempo_restante_moeda2x = max(0, self.tempoTotalPowerUpMoeda2x // 1000 - tempo_decorrido_moeda2x)

            for powerUp in self.PowerUpsAtivos:
                if powerUp[0] == 'moeda2x':
                    segundos_moeda2x = int(tempo_restante_moeda2x % 60)
                    powerUp[2] = segundos_moeda2x

    




        # Código para mostrar o timer de cada PowerUP de forma Dinâmica




        """
        Código Backup caso dê merda com o outro jeito abaixo
        
        if self.powerUp_velocidade_ativo and self.tempo_inicioPowerUpVelocidade:
            timer_PowerUpVelocidade = test_font.render(f'Velocidade por {segundos_velocidade} s', False, 'yellow')
            timer_PowerUpVelocidade_rect = timer_PowerUpVelocidade.get_rect(topleft=(0, 100))
            screen.blit(timer_PowerUpVelocidade,timer_PowerUpVelocidade_rect)


        if self.powerUp_Teste_ativo and self.tempo_inicioPowerUpTeste:
            timer_PowerUpTeste = test_font.render(f'Teste por {segundos_teste} s', False, 'green')
            timer_PowerUpTeste_rect = timer_PowerUpTeste.get_rect(topleft=(0, 132))
            screen.blit(timer_PowerUpTeste, timer_PowerUpTeste_rect)
        """

        start_y = 100
        spacing = 32

        for i, (nome, cor, segundos) in enumerate(self.PowerUpsAtivos):
            texto = config.test_font.render(f"{nome} por {segundos} s", False, cor)
            texto_rect = texto.get_rect(topleft=(5, start_y + i * spacing))  # Ajuste dinâmico
            config.screen.blit(texto, texto_rect)



    def update(self):
        self.player_input()
        self.colisaoMoeda()
        self.colisaoBomba()
        self.tempo_restante()
        self.colisaoPowerUp()
        self.poderPowerUp()
        self.verificar_tempo()
        self.mostrarVida()


#Instancia da classe Player
player = pygame.sprite.GroupSingle()
player.add(Player())