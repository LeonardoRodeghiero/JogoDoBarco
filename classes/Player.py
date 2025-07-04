import pygame
import config
import audio
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, player_id=0):
        super().__init__()
        if player_id == 0:
            player1 = pygame.image.load('graficos/barco/barco1.png').convert_alpha()
            player2 = pygame.image.load('graficos/barco/barco2.png').convert_alpha()
            player3 = pygame.image.load('graficos/barco/barco3.png').convert_alpha()
            player4 = pygame.image.load('graficos/barco/barco4.png').convert_alpha()
            player5 = pygame.image.load('graficos/barco/barco5.png').convert_alpha()
            player6 = pygame.image.load('graficos/barco/barco6.png').convert_alpha()
            player7 = pygame.image.load('graficos/barco/barco7.png').convert_alpha()
            player8 = pygame.image.load('graficos/barco/barco8.png').convert_alpha()
            player9 = pygame.image.load('graficos/barco/barco9.png').convert_alpha()
        else:
            if player_id == 1:
                player1 = pygame.image.load('graficos/barco/player1/barco1_p1.png').convert_alpha()
                player2 = pygame.image.load('graficos/barco/player1/barco2_p1.png').convert_alpha()
                player3 = pygame.image.load('graficos/barco/player1/barco3_p1.png').convert_alpha()
                player4 = pygame.image.load('graficos/barco/player1/barco4_p1.png').convert_alpha()
                player5 = pygame.image.load('graficos/barco/player1/barco5_p1.png').convert_alpha()
                player6 = pygame.image.load('graficos/barco/player1/barco6_p1.png').convert_alpha()
                player7 = pygame.image.load('graficos/barco/player1/barco7_p1.png').convert_alpha()
                player8 = pygame.image.load('graficos/barco/player1/barco8_p1.png').convert_alpha()
                player9 = pygame.image.load('graficos/barco/player1/barco9_p1.png').convert_alpha() 
            if player_id == 2:
                player1 = pygame.image.load('graficos/barco/player2/barco1_p2.png').convert_alpha()
                player2 = pygame.image.load('graficos/barco/player2/barco2_p2.png').convert_alpha()
                player3 = pygame.image.load('graficos/barco/player2/barco3_p2.png').convert_alpha()
                player4 = pygame.image.load('graficos/barco/player2/barco4_p2.png').convert_alpha()
                player5 = pygame.image.load('graficos/barco/player2/barco5_p2.png').convert_alpha()
                player6 = pygame.image.load('graficos/barco/player2/barco6_p2.png').convert_alpha()
                player7 = pygame.image.load('graficos/barco/player2/barco7_p2.png').convert_alpha()
                player8 = pygame.image.load('graficos/barco/player2/barco8_p2.png').convert_alpha()
                player9 = pygame.image.load('graficos/barco/player2/barco9_p2.png').convert_alpha() 
        self.frames = [player1, player2, player3, player4, player5, player6, player7, player8, player9]
        self.player_index = 0

        self.id = player_id

        self.peso = 0
        self.pontuacao = 0
        self.pontos = 0
        self.vidaAtual = 3
        self.escudoAtivo = 0
        self.toxicidade = 0
        self.PowerUpsAtivos = []
        self.debuffsAtivos = []
        self.pesoExtra = 0

        #Recuperacao
        self.intervalo = 200  # em milissegundos
        self.duracao_piscada = 3000  # Tempo total de piscada em milissegundos
        self.inicio_piscada = 0
        self.ultimo_tempo = 0  
        self.visivel = True
        self.piscando = False

        #Velocidade
        self.velocidadeNormal = 10
        self.velocidadeBase = max(1, self.velocidadeNormal - self.peso + self.pesoExtra)
        self.velocidade = self.velocidadeBase

        # icons
        self.coracaoCheio = pygame.image.load('graficos/coracao/coracaoCheio.png')
        self.coracaoVazio = pygame.image.load('graficos/coracao/coracaoVazio.png')

        self.coracaoCheio = pygame.transform.scale(self.coracaoCheio, (45,50))
        self.coracaoVazio = pygame.transform.scale(self.coracaoVazio, (45,50))

        self.escudoCheio = pygame.image.load('graficos/powerUps/escudo/escudo_1.png')
        self.escudoVazio = pygame.image.load('graficos/powerUps/escudo/escudo_Vazio.xcf')

        self.escudoCheio = pygame.transform.scale(self.escudoCheio, (45,50))
        self.escudoVazio = pygame.transform.scale(self.escudoVazio, (45,50))

        self.toxicidade_icon = pygame.image.load('graficos/toxicidade/toxico.png')
        self.toxicidade_icon = pygame.transform.scale(self.toxicidade_icon, (48,45))

        # POWER UPS

        # Atributos PowerUps de velocidade
        self.powerUp_velocidade_ativo = False
        self.tempo_inicioPowerUpVelocidade = None
        self.tempoTotalPowerUpVelocidade = 15000


        # Atributos PowerUps de invulnerabilidade
        self.powerUp_invulnerabilidade_ativo = False
        self.tempo_inicioPowerUpinvulnerabilidade = None
        self.tempoTotalPowerUpinvulnerabilidade = 15000

        # Atributos PowerUps de moeda x2
        self.powerUp_moeda2x_ativo = False
        self.tempo_inicioPowerUpMoeda2x = None
        self.tempoTotalPowerUpMoeda2x = 15000
        self.multMoeda2x = 1

        # DEBUFFS

        # Atributos Debuff de congelamento
        self.debuff_congelamento_ativo = False
        self.tempo_inicioDebuffCongelamento = None
        self.tempototalDebuffCongelamento = 2000

        # Atributos debuff de lentidao
        self.debuff_lentidao_ativo = False
        self.tempo_inicioDebuffLentidao = None
        self.tempototalDebuffLentidao = 15000

        # atirbutos debuff de moedas divididas por 2
        self.debuff_moedadiv2_ativo = False
        self.tempo_inicioDebuffmoedadiv2 = None
        self.tempototalDebuffmoedadiv2 = 15000
        self.divmoeda = 1

        self.image = self.frames[self.player_index]
        self.rect = self.image.get_rect(midbottom=(x, y))
    
    def iniciar_piscada(self):
        self.piscando = True
        self.inicio_piscada = pygame.time.get_ticks()
        self.ultimo_tempo = self.inicio_piscada
        self.visivel = True  # Começa visível
        if self.vidaAtual > 0:
            audio.tocar_som_recuperacao()

    def atualizar_velocidade_base(self):
        if self.powerUp_velocidade_ativo == True:
            base = (self.velocidadeNormal - self.peso + self.pesoExtra) + 2
            self.velocidadeBase = max(2, base)

        if self.debuff_lentidao_ativo == True:
            base = (self.velocidadeNormal - self.peso + self.pesoExtra) / 2
            self.velocidadeBase = max(2, base)

        if self.powerUp_velocidade_ativo == False and self.debuff_lentidao_ativo == False:
            base = self.velocidadeNormal - self.peso + self.pesoExtra
            self.velocidadeBase = max(2, base)  # Garante um mínimo pra base ficar funcional

    def player_input(self):

        keys = pygame.key.get_pressed()
        animacao = self.velocidade / 50
        if self.id == 0:
            if self.debuff_congelamento_ativo == False:
                if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                    pass
                else:
                    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right <= config.largura:
                        self.player_index += animacao
                        if self.player_index >= 9:
                            self.player_index = 0
                        self.image = self.frames[int(self.player_index)]

                        if(keys[pygame.K_LSHIFT]): self.rect.x += self.velocidade * 0.5
                        else: self.rect.x += self.velocidade

                    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left >= 0:
                        self.player_index -= animacao
                        if self.player_index < 0:
                            self.player_index = 8
                        self.image = self.frames[int(self.player_index)]

                        if(keys[pygame.K_LSHIFT]): self.rect.x -= self.velocidade * 0.5
                        else: self.rect.x -= self.velocidade
                    else:
                        self.player_index = int(self.player_index)
        else:
            if self.id == 1:
                if self.debuff_congelamento_ativo == False:
                    if keys[pygame.K_a] and keys[pygame.K_d]:
                        pass
                    else:
                        if (keys[pygame.K_d]) and self.rect.right <= config.largura:
                            self.player_index += animacao
                            if self.player_index >= 9:
                                self.player_index = 0
                            self.image = self.frames[int(self.player_index)]

                            if(keys[pygame.K_LSHIFT]): self.rect.x += self.velocidade * 0.5
                            else: self.rect.x += self.velocidade
                        elif (keys[pygame.K_a]) and self.rect.left >= 0:
                            self.player_index -= animacao
                            if self.player_index < 0:
                                self.player_index = 8
                            self.image = self.frames[int(self.player_index)]

                            if(keys[pygame.K_LSHIFT]): self.rect.x -= self.velocidade * 0.5
                            else: self.rect.x -= self.velocidade
                        else:
                            self.player_index = int(self.player_index)
            if self.id == 2:
                if self.debuff_congelamento_ativo == False:
                    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                        pass
                    else:
                        if (keys[pygame.K_RIGHT]) and self.rect.right <= config.largura:
                                self.player_index += animacao
                                if self.player_index >= 9:
                                    self.player_index = 0
                                self.image = self.frames[int(self.player_index)]

                                if(keys[pygame.K_RSHIFT]): self.rect.x += self.velocidade * 0.5
                                else: self.rect.x += self.velocidade
                        elif (keys[pygame.K_LEFT]) and self.rect.left >= 0:
                            self.player_index -= animacao
                            if self.player_index < 0:
                                self.player_index = 8
                            self.image = self.frames[int(self.player_index)]

                            if(keys[pygame.K_RSHIFT]): self.rect.x -= self.velocidade * 0.5
                            else: self.rect.x -= self.velocidade
                        else:
                            self.player_index = int(self.player_index)

    def entoxicar(self, lvl_toxico = 1):
        self.toxicidade += lvl_toxico
        audio.entoxicar()
        if self.toxicidade >= 3:
            self.toxicidade = 0
            self.vidaAtual -= 1
            self.iniciar_piscada()

    def mostrarVida(self):
        if self.id == 0:
            pos_x_coracao = 5
            if self.vidaAtual == 3:
                self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
                config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)

                pos_x_coracao += 45 + 8
                self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
                config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                pos_x_coracao += 45 + 8

                self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
                config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
            elif self.vidaAtual == 2:
                pos_x_coracao = 0
                self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
                config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                pos_x_coracao += 45 + 8

                self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
                config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)

                pos_x_coracao += 45 + 8

                self.coracaoVazio_rect = self.coracaoVazio.get_rect(topleft=(pos_x_coracao,7))
                config.screen.blit(self.coracaoVazio, self.coracaoVazio_rect)
            elif self.vidaAtual == 1:
                pos_x_coracao = 0
                self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,7))
                config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                pos_x_coracao += 45 + 8

                self.coracaoVazio_rect = self.coracaoVazio.get_rect(topleft=(pos_x_coracao,7))
                config.screen.blit(self.coracaoVazio, self.coracaoVazio_rect)

                pos_x_coracao += 45 + 8

                self.coracaoVazio_rect = self.coracaoVazio.get_rect(topleft=(pos_x_coracao,7))
                config.screen.blit(self.coracaoVazio, self.coracaoVazio_rect)

            pos_x_escudo = pos_x_coracao + 45 + 8
            if self.escudoAtivo == 1:
                self.escudoCheio_rect = self.escudoCheio.get_rect(topleft=(pos_x_escudo,7))
                config.screen.blit(self.escudoCheio, self.escudoCheio_rect)
            else:
                self.escudoVazio_rect = self.escudoVazio.get_rect(topleft=(pos_x_escudo,7))
                config.screen.blit(self.escudoVazio, self.escudoVazio_rect)
        else:
            if self.id == 1:
                pos_x_coracao = 5
                if self.vidaAtual == 3:
                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)

                    pos_x_coracao += 45 + 8
                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                    pos_x_coracao += 45 + 8

                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                elif self.vidaAtual == 2:
                    pos_x_coracao = 0
                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                    pos_x_coracao += 45 + 8

                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)

                    pos_x_coracao += 45 + 8

                    self.coracaoVazio_rect = self.coracaoVazio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoVazio, self.coracaoVazio_rect)
                elif self.vidaAtual == 1:
                    pos_x_coracao = 0
                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                    pos_x_coracao += 45 + 8

                    self.coracaoVazio_rect = self.coracaoVazio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoVazio, self.coracaoVazio_rect)

                    pos_x_coracao += 45 + 8

                    self.coracaoVazio_rect = self.coracaoVazio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoVazio, self.coracaoVazio_rect)


                pos_x_escudo = pos_x_coracao + 45 + 8
                if self.escudoAtivo == 1:
                    self.escudoCheio_rect = self.escudoCheio.get_rect(topleft=(pos_x_escudo,45))
                    config.screen.blit(self.escudoCheio, self.escudoCheio_rect)
                else:
                    self.escudoVazio_rect = self.escudoVazio.get_rect(topleft=(pos_x_escudo,45))
                    config.screen.blit(self.escudoVazio, self.escudoVazio_rect)

            if self.id == 2:
                pos_x_coracao = config.largura - 217 - 5
                if self.vidaAtual == 3:
                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)

                    pos_x_coracao += 45 + 8
                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                    pos_x_coracao += 45 + 8

                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                elif self.vidaAtual == 2:
                    #pos_x_coracao = 0
                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                    pos_x_coracao += 45 + 8

                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)

                    pos_x_coracao += 45 + 8

                    self.coracaoVazio_rect = self.coracaoVazio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoVazio, self.coracaoVazio_rect)
                elif self.vidaAtual == 1:
                    #pos_x_coracao = 0
                    self.coracaoCheio_rect = self.coracaoCheio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoCheio, self.coracaoCheio_rect)
                    pos_x_coracao += 45 + 8

                    self.coracaoVazio_rect = self.coracaoVazio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoVazio, self.coracaoVazio_rect)

                    pos_x_coracao += 45 + 8

                    self.coracaoVazio_rect = self.coracaoVazio.get_rect(topleft=(pos_x_coracao,45))
                    config.screen.blit(self.coracaoVazio, self.coracaoVazio_rect)


                pos_x_escudo = pos_x_coracao + 45 + 8
                if self.escudoAtivo == 1:
                    self.escudoCheio_rect = self.escudoCheio.get_rect(topleft=(pos_x_escudo,45))
                    config.screen.blit(self.escudoCheio, self.escudoCheio_rect)
                else:
                    self.escudoVazio_rect = self.escudoVazio.get_rect(topleft=(pos_x_escudo,45))
                    config.screen.blit(self.escudoVazio, self.escudoVazio_rect)

    def desenhaToxicidade(self, barra_x, barra_y):
        slot_width = 20
        slot_height = 10
        espacamento = 2

        for i in range(3):
            rect = pygame.Rect(barra_x + i * (slot_width + espacamento), barra_y, slot_width, slot_height)
            if i < self.toxicidade:
                pygame.draw.rect(config.screen, (255, 255, 0), rect)  # amarelo
            else:
                pygame.draw.rect(config.screen, (180, 180, 180), rect)  # cinza claro
            pygame.draw.rect(config.screen, (0, 0, 0), rect, 2)  # contorno

            icon_x = barra_x - 3 * (slot_width + espacamento) + 10
            config.screen.blit(self.toxicidade_icon, (icon_x, barra_y - 20))

    def mostrarToxicidade(self):
        if self.id == 0:
            self.desenhaToxicidade(60, 80)
        elif self.id == 1:
            self.desenhaToxicidade(60, 110)
        else:
            self.desenhaToxicidade(920, 110)

    def colisaoMoeda(self):

        if self.peso - self.pesoExtra < 8:

            moeda_colidida = pygame.sprite.spritecollide(self, config.moeda_group, True)
            for moeda in moeda_colidida:
                if moeda.tipo == 'ouro':
                    self.peso += 0.5

                    self.pontos += 3 * self.multMoeda2x // self.divmoeda

                    audio.escolher_som_moeda_e_tocar()

                if moeda.tipo == 'prata':
                    self.peso += 0.3
                    self.pontos += 2 * self.multMoeda2x // self.divmoeda
                    audio.escolher_som_moeda_e_tocar()

                if moeda.tipo == 'bronze':
                    self.peso += 0.1
                    self.pontos += 1 * self.multMoeda2x // self.divmoeda
                    audio.escolher_som_moeda_e_tocar()
        
    def colisaoInimigo(self):
        if self.powerUp_invulnerabilidade_ativo == False and self.piscando == False:
            inimigo_colidido = pygame.sprite.spritecollide(self, config.inimigo_group, True)
            for inimigo in inimigo_colidido:
                if self.escudoAtivo == 0:
                    if inimigo.tipo == 'bomba' :
                        self.vidaAtual -= 1
                        self.iniciar_piscada()
                        audio.tocar_som_explosao()

                    if inimigo.tipo == 'flecha':
                        self.vidaAtual -= 1
                        self.iniciar_piscada()
                        audio.tocar_som_flechada()

                    if inimigo.tipo == 'barrilRadioativo':
                        self.vidaAtual -= 1
                        self.entoxicar(2)
                        self.iniciar_piscada()
                        audio.tocar_som_explosao_radiacao()
                else:
                    if inimigo.tipo == 'bomba':
                        self.escudoAtivo = 0
                        self.iniciar_piscada()
                        audio.tocar_som_explosao()

                    if inimigo.tipo == 'flecha':
                        self.escudoAtivo = 0
                        self.iniciar_piscada()
                        audio.tocar_som_flechada()

                    if inimigo.tipo == 'barrilRadioativo':
                        self.escudoAtivo = 0
                        self.entoxicar(2)
                        self.iniciar_piscada()
                        audio.tocar_som_explosao_radiacao()


    def colisaoDebuff(self):
        from tempo import retirarTempo
        if self.powerUp_invulnerabilidade_ativo == False and self.piscando == False:

            debuff_colidido = pygame.sprite.spritecollide(self, config.debuff_group, True)

            for debuff in debuff_colidido:
                if debuff.tipo == 'congelamento':
                    self.ativar_debuff('congelamento')
                    audio.tocar_som_congelamento()
                if debuff.tipo == 'lentidao':
                    self.ativar_debuff('lentidao')
                    audio.tocar_som_debuff()

                if debuff.tipo == 'menostempo':
                    retirarTempo(10)
                    audio.tocar_som_debuff()

                if debuff.tipo == 'moedas valem menos':
                    self.ativar_debuff('moedas valem menos')
                    audio.tocar_som_debuff()

    def ativar_debuff(self, debuff_tipo):
        if debuff_tipo == 'congelamento':
            if self.debuff_congelamento_ativo == False:
                self.debuffsAtivos.append(['congelamento', 'white', 0])

            self.debuff_congelamento_ativo = True
            self.tempo_inicioDebuffCongelamento = pygame.time.get_ticks()

        if debuff_tipo == 'lentidao':
            if self.debuff_lentidao_ativo== False:
                self.debuffsAtivos.append(['lentidao', 'purple', 0])

            self.debuff_lentidao_ativo = True
            self.tempo_inicioDebuffLentidao = pygame.time.get_ticks()

        if debuff_tipo == 'moedas valem menos':
            if self.debuff_moedadiv2_ativo== False:
                self.debuffsAtivos.append(['moedas valem menos', 'pink', 0])

            self.debuff_moedadiv2_ativo = True
            self.tempo_inicioDebuffmoedadiv2 = pygame.time.get_ticks()

    def poderDebuff(self):
        for debuff in self.debuffsAtivos:
            if debuff[0] == 'congelamento':
                imagem_base = self.frames[int(self.player_index)].copy()
        
                # Criar overlay azul claro do mesmo tamanho, totalmente transparente
                overlay = pygame.Surface(imagem_base.get_size(), pygame.SRCALPHA)
                overlay.fill((180, 240, 255, 0))  # Totalmente transparente a princípio

                # Acessar os pixels da imagem base
                for y in range(imagem_base.get_height()):
                    for x in range(imagem_base.get_width()):
                        r, g, b, a = imagem_base.get_at((x, y))
                        if a != 0:  # Só se o pixel for visível
                            overlay.set_at((x, y), (190, 230, 250, 90))  # Azul claro no pixel visível

                # Aplica o overlay pixel a pixel
                imagem_base.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

                self.image = imagem_base  

            if debuff[0] == 'moedas valem menos':
                self.divmoeda = 2
            
        if self.debuff_congelamento_ativo == False:
            #Voltar ao normal AQUI
            self.image = self.frames[int(self.player_index)]

        if self.debuff_moedadiv2_ativo == False:
            self.divmoeda = 1
    
    def morrer(self):
        if self.vidaAtual <= 0:
            self.kill()

    def verificar_area_congelada(self):
        colisoes = pygame.sprite.spritecollide(self, config.area_congelada_group, False)
        if colisoes:
            self.velocidade = max(1, self.velocidadeBase / 2)
        elif not self.debuff_congelamento_ativo:
            self.velocidade = self.velocidadeBase

    def verificar_area_radioativa(self):
        colisoes = pygame.sprite.spritecollide(self, config.area_radioativa_group, False)
        if self.piscando == False:
            colisoes = pygame.sprite.spritecollide(self, config.area_radioativa_group, True)
            if colisoes:
                self.entoxicar()        
    
    def verificar_tempo_Debuff(self):
        if self.debuff_congelamento_ativo and self.tempo_inicioDebuffCongelamento:
            tempo_decorrido_congelamento = pygame.time.get_ticks() - self.tempo_inicioDebuffCongelamento
            if tempo_decorrido_congelamento >= self.tempototalDebuffCongelamento:  # 15 segundos em milissegundos
                self.debuff_congelamento_ativo = False  # Desativa a habilidade
                
                self.debuffsAtivos = [d for d in self.debuffsAtivos if d[0] != "congelamento"]

        if self.debuff_lentidao_ativo and self.tempo_inicioDebuffLentidao:
            tempo_decorrido_lentidao = pygame.time.get_ticks() - self.tempo_inicioDebuffLentidao
            if tempo_decorrido_lentidao >= self.tempototalDebuffLentidao:  # 15 segundos em milissegundos
                self.debuff_lentidao_ativo = False  # Desativa a habilidade
                
                self.debuffsAtivos = [d for d in self.debuffsAtivos if d[0] != "lentidao"]

        if self.debuff_moedadiv2_ativo and self.tempo_inicioDebuffmoedadiv2:
            tempo_decorrido_moedadiv2 = pygame.time.get_ticks() - self.tempo_inicioDebuffmoedadiv2
            if tempo_decorrido_moedadiv2 >= self.tempototalDebuffmoedadiv2:  # 15 segundos em milissegundos
                self.debuff_moedadiv2_ativo = False  # Desativa a habilidade
                
                self.debuffsAtivos = [d for d in self.debuffsAtivos if d[0] != "moedas valem menos"]

    def tempo_restante_Debuff(self):
        if self.debuff_congelamento_ativo and self.tempo_inicioDebuffCongelamento:
            tempo_decorrido_congelamento = (pygame.time.get_ticks() - self.tempo_inicioDebuffCongelamento) // 1000
            tempo_restante_congelamento = max(0, self.tempototalDebuffCongelamento // 1000 - tempo_decorrido_congelamento)


            for debuff in self.debuffsAtivos:
                if debuff[0] == 'congelamento':
                    segundos_congelamento = int(tempo_restante_congelamento % 60)
                    debuff[2] = segundos_congelamento

        if self.debuff_lentidao_ativo and self.tempo_inicioDebuffLentidao:
            tempo_decorrido_lentidao = (pygame.time.get_ticks() - self.tempo_inicioDebuffLentidao) // 1000
            tempo_restante_lentidao = max(0, self.tempototalDebuffLentidao // 1000 - tempo_decorrido_lentidao)


            for debuff in self.debuffsAtivos:
                if debuff[0] == 'lentidao':
                    segundos_lentidao = int(tempo_restante_lentidao % 60)
                    debuff[2] = segundos_lentidao

        if self.debuff_moedadiv2_ativo and self.tempo_inicioDebuffmoedadiv2:
            tempo_decorrido_moedadiv2 = (pygame.time.get_ticks() - self.tempo_inicioDebuffmoedadiv2) // 1000
            tempo_restante_moedadiv2 = max(0, self.tempototalDebuffmoedadiv2 // 1000 - tempo_decorrido_moedadiv2)


            for debuff in self.debuffsAtivos:
                if debuff[0] == 'moedas valem menos':
                    segundos_moedadiv2 = int(tempo_restante_moedadiv2 % 60)
                    debuff[2] = segundos_moedadiv2

    def colisaoPowerUp(self):
        from tempo import adicionarTempo

        power_up_colidido = pygame.sprite.spritecollide(self, config.powerup_group, True)

        for powerUp in power_up_colidido:
            if powerUp.tipo == 'vida':
                if self.vidaAtual < 3:
                    self.vidaAtual += 1
                audio.tocar_som_powerup()

            if powerUp.tipo == 'velocidade':
                self.ativar_power_up('velocidade')
                audio.tocar_som_powerup()


            if powerUp.tipo == 'invulnerabilidade':            
                self.ativar_power_up('invulnerabilidade')
                audio.tocar_som_powerup()
            
            if powerUp.tipo == 'moeda2x':
                self.ativar_power_up('moeda2x')
                audio.tocar_som_powerup()

            if powerUp.tipo == 'tempo':
                adicionarTempo(10)
                audio.tocar_som_powerup()

            if powerUp.tipo == 'pesoExtra':
                self.pesoExtra += 0.5
                audio.tocar_som_powerup()

            if powerUp.tipo == 'escudo':
                self.escudoAtivo = 1
                audio.tocar_som_powerup()

    def ativar_power_up(self, powerUpTipo):
        """Ativa a habilidade temporária"""
        if powerUpTipo == 'velocidade':
            if self.powerUp_velocidade_ativo == False:
                self.PowerUpsAtivos.append(['velocidade', 'yellow', 0])

            self.powerUp_velocidade_ativo = True
            self.tempo_inicioPowerUpVelocidade = pygame.time.get_ticks()  # Guarda o tempo inicial

        if powerUpTipo =='invulnerabilidade':
            if self.powerUp_invulnerabilidade_ativo == False:
                self.PowerUpsAtivos.append(['invulnerabilidade', (75,188,250), 0])

            self.powerUp_invulnerabilidade_ativo = True
            self.tempo_inicioPowerUpinvulnerabilidade = pygame.time.get_ticks()  # Guarda o tempo inicial


        if powerUpTipo == 'moeda2x':
            if self.powerUp_moeda2x_ativo == False:
                self.PowerUpsAtivos.append(['moeda2x', 'orange', 0])
            
            self.powerUp_moeda2x_ativo = True
            self.tempo_inicioPowerUpMoeda2x = pygame.time.get_ticks()



    def poderPowerUp(self):

        for powerUp in self.PowerUpsAtivos:
            """    if powerUp[0] == 'velocidade':
                self.velocidade = max(1, self.velocidadeBase + 10)
            """
            if powerUp[0] == 'moeda2x':
                self.multMoeda2x = 2

            if powerUp[0] == 'invulnerabilidade':
                self.image.set_alpha(128)


        if self.powerUp_velocidade_ativo == False:
            self.velocidade = self.velocidadeBase

        if self.powerUp_moeda2x_ativo == False:
            self.multMoeda2x = 1

        if self.powerUp_invulnerabilidade_ativo == False:
            self.image.set_alpha(255)

    def verificar_tempo_PowerUp(self):
        """Verifica se os 15 segundos já passaram"""
        if self.powerUp_velocidade_ativo and self.tempo_inicioPowerUpVelocidade:
            tempo_decorrido_velocidade = pygame.time.get_ticks() - self.tempo_inicioPowerUpVelocidade
            if tempo_decorrido_velocidade >= self.tempoTotalPowerUpVelocidade:  # 15 segundos em milissegundos
                self.powerUp_velocidade_ativo = False  # Desativa a habilidade
                
                self.PowerUpsAtivos = [p for p in self.PowerUpsAtivos if p[0] != "velocidade"]


        if self.powerUp_invulnerabilidade_ativo and self.tempo_inicioPowerUpinvulnerabilidade:
            tempo_decorrido_invulnerabilidade = pygame.time.get_ticks() - self.tempo_inicioPowerUpinvulnerabilidade
            if tempo_decorrido_invulnerabilidade >= self.tempoTotalPowerUpinvulnerabilidade:  # 15 segundos em milissegundos
                self.powerUp_invulnerabilidade_ativo = False  # Desativa a habilidade
                self.PowerUpsAtivos = [p for p in self.PowerUpsAtivos if p[0] != "invulnerabilidade"]
    

        if self.powerUp_moeda2x_ativo and self.tempo_inicioPowerUpMoeda2x:
            tempo_decorrido_moeda2x = pygame.time.get_ticks() - self.tempo_inicioPowerUpMoeda2x
            if tempo_decorrido_moeda2x >= self.tempoTotalPowerUpMoeda2x:  # 15 segundos em milissegundos
                self.powerUp_moeda2x_ativo = False  # Desativa a habilidade
                self.PowerUpsAtivos = [p for p in self.PowerUpsAtivos if p[0] != "moeda2x"]
    


    def tempo_restante_PowerUp(self):
        """Retorna o tempo restante"""
        if self.powerUp_velocidade_ativo and self.tempo_inicioPowerUpVelocidade:
            tempo_decorrido_velocidade = (pygame.time.get_ticks() - self.tempo_inicioPowerUpVelocidade) // 1000
            tempo_restante_velocidade = max(0, self.tempoTotalPowerUpVelocidade // 1000 - tempo_decorrido_velocidade)


            for powerUp in self.PowerUpsAtivos:
                if powerUp[0] == 'velocidade':
                    segundos_velocidade = int(tempo_restante_velocidade % 60)
                    powerUp[2] = segundos_velocidade

        if self.powerUp_invulnerabilidade_ativo and self.tempo_inicioPowerUpinvulnerabilidade:
            tempo_decorrido_invulnerabilidade = (pygame.time.get_ticks() - self.tempo_inicioPowerUpinvulnerabilidade) // 1000
            tempo_restante_invulnerabilidade = max(0, self.tempoTotalPowerUpinvulnerabilidade // 1000 - tempo_decorrido_invulnerabilidade)


            for powerUp in self.PowerUpsAtivos:
                if powerUp[0] == 'invulnerabilidade':
                    segundos_invulnerabilidade = int(tempo_restante_invulnerabilidade % 60)
                    powerUp[2] = segundos_invulnerabilidade

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
        if self.id == 0:
            start_y = 100
            spacing = 32

            for i, (nome, cor, segundos) in enumerate(self.PowerUpsAtivos):
                texto = config.test_font.render(f"{nome} por {segundos} s", False, cor)
                texto_rect = texto.get_rect(topleft=(5, start_y + i * spacing))  # Ajuste dinâmico
                config.screen.blit(texto, texto_rect)

            start_y_debuff = 100
            spacing_debuff = 32

            for i, (nome, cor, segundos) in enumerate(self.debuffsAtivos):
                texto_debuff = config.test_font.render(f"{nome} por {segundos} s", False, cor)
                texto_debuff_rect = texto_debuff.get_rect(topright=(config.largura - 5, start_y_debuff + i * spacing_debuff))  # Ajuste dinâmico
                config.screen.blit(texto_debuff, texto_debuff_rect)
        else:
            if self.id == 1:
                start_y = 150
                spacing = 32

                for i, (nome, cor, segundos) in enumerate(self.PowerUpsAtivos):
                    texto = config.powerUp_debuff_font.render(f"{nome} por {segundos} s", False, cor)
                    texto_rect = texto.get_rect(topleft=(5, start_y + i * spacing))  # Ajuste dinâmico
                    config.screen.blit(texto, texto_rect)

                start_y_debuff = 250
                spacing_debuff = 32

                for i, (nome, cor, segundos) in enumerate(self.debuffsAtivos):
                    texto_debuff = config.powerUp_debuff_font.render(f"{nome} por {segundos} s", False, cor)
                    texto_debuff_rect = texto_debuff.get_rect(topleft=(5, start_y_debuff + i * spacing_debuff))  # Ajuste dinâmico
                    config.screen.blit(texto_debuff, texto_debuff_rect)

            if self.id == 2:
                start_y = 150
                spacing = 32

                for i, (nome, cor, segundos) in enumerate(self.PowerUpsAtivos):
                    texto = config.powerUp_debuff_font.render(f"{nome} por {segundos} s", False, cor)
                    texto_rect = texto.get_rect(topright=(config.largura - 5, start_y + i * spacing))  # Ajuste dinâmico
                    config.screen.blit(texto, texto_rect)

                start_y_debuff = 250
                spacing_debuff = 32

                for i, (nome, cor, segundos) in enumerate(self.debuffsAtivos):
                    texto_debuff = config.powerUp_debuff_font.render(f"{nome} por {segundos} s", False, cor)
                    texto_debuff_rect = texto_debuff.get_rect(topright=(config.largura - 5, start_y_debuff + i * spacing_debuff))  # Ajuste dinâmico
                    config.screen.blit(texto_debuff, texto_debuff_rect)
    def update(self):
        self.atualizar_velocidade_base()
        self.player_input()
        self.colisaoMoeda()
        self.colisaoInimigo()
        self.colisaoDebuff()
        self.poderDebuff()
        self.verificar_tempo_Debuff()
        self.tempo_restante_Debuff()
        self.tempo_restante_PowerUp()
        self.colisaoPowerUp()
        self.poderPowerUp()
        self.verificar_tempo_PowerUp()
        self.mostrarVida()
        self.mostrarToxicidade()
        self.verificar_area_congelada()
        self.verificar_area_radioativa()
        self.morrer()
        tempo_atual = pygame.time.get_ticks()
        
        if self.piscando:
            if tempo_atual - self.inicio_piscada >= self.duracao_piscada:
                self.piscando = False
                self.visivel = True  # Garante que fique visível ao final
            elif tempo_atual - self.ultimo_tempo >= self.intervalo:
                self.visivel = not self.visivel
                self.ultimo_tempo = tempo_atual

    def draw(self, surface):
        if self.visivel:
            surface.blit(self.image, self.rect)