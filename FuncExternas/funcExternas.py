import pygame, config
from classes.Player import player





"""def escolher_fundo(fundoSorteado):
    cor_score = ()
    if fundoSorteado == 1:
        fundo_surf = pygame.image.load('graficos/fundo/fundo1.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))

        cor_score =  (64,64,64)
    if fundoSorteado == 2:
        fundo_surf = pygame.image.load('graficos/fundo/fundo2.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))

        cor_score =  (64,64,64)

    if fundoSorteado == 3:
        fundo_surf = pygame.image.load('graficos/fundo/fundo3.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))

        cor_score =  'white'

    if fundoSorteado == 4:
        fundo_surf = pygame.image.load('graficos/fundo/fundo4.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura)) 

        cor_score =  'white'


    if fundoSorteado == 5:
        fundo_surf = pygame.image.load('graficos/fundo/fundo5.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura)) 

        cor_score =  (64,64,64)


    if fundoSorteado == 6:
        fundo_surf = pygame.image.load('graficos/fundo/fundo6.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))  

        cor_score =  'white'


    if fundoSorteado == 7:
        fundo_surf = pygame.image.load('graficos/fundo/fundo7.png').convert()
        fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))

        cor_score =  (64,64,64)


    return fundo_surf, cor_score"""

def escolher_fundo(fundoSorteado):
    cor_score = ()
    """"
    if fundoSorteado == 1:
    fundo_surf = pygame.image.load('graficos/fundo/fundo1.png').convert()
    fundo_surf = pygame.transform.scale(fundo_surf, (config.largura, config.altura))

    cor_score =  (64,64,64)
    """
    
    if fundoSorteado == 2:
        lista_de_camadas = [
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo2/sombras.png').convert_alpha(), "velocidade": 0.05},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo2/ceu-mar.png').convert_alpha(), "velocidade": 0.1},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo2/nuvens.png').convert_alpha(), "velocidade": 0.3}
            
        ]
        fundo_atual = []
        for camada in lista_de_camadas:
            imagem = camada["imagem"]
            velocidade = camada["velocidade"]
            imagem = pygame.transform.scale(imagem, (config.largura, config.altura))
            fundo_atual.append({
                "imagem": imagem,
                "velocidade": velocidade,
                "y": 0
            })

        cor_score =  (64,64,64)
    if fundoSorteado == 3:
        lista_de_camadas = [
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo3/ceu-mar.png').convert_alpha(), "velocidade": 0.1},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo3/lua.png').convert_alpha(), "velocidade": 0.05},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo3/nuvens.png').convert_alpha(), "velocidade": 0.3},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo3/sombras.png').convert_alpha(), "velocidade": 0.6}
            

        ]
        fundo_atual = []
        for camada in lista_de_camadas:
            imagem = camada["imagem"]
            velocidade = camada["velocidade"]
            imagem = pygame.transform.scale(imagem, (config.largura, config.altura))
            fundo_atual.append({
                "imagem": imagem,
                "velocidade": velocidade,
                "y": 0
            })

        cor_score =  'white'
    if fundoSorteado == 4:
        lista_de_camadas = [
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo4/ceu-mar.png').convert_alpha(), "velocidade": 0.05},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo4/nuvens.png').convert_alpha(), "velocidade": 0.25},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo4/sombras.png').convert_alpha(), "velocidade": 0.28}
            

        ]
        fundo_atual = []
        for camada in lista_de_camadas:
            imagem = camada["imagem"]
            velocidade = camada["velocidade"]
            imagem = pygame.transform.scale(imagem, (config.largura, config.altura))
            fundo_atual.append({
                "imagem": imagem,
                "velocidade": velocidade,
                "y": 0
            })
        cor_score =  'white'

    if fundoSorteado == 5:
        lista_de_camadas = [
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo5/ceu-mar.png').convert_alpha(), "velocidade": 0.05},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo5/nuvens.png').convert_alpha(), "velocidade": 0.15},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo5/pedra-atras.png').convert_alpha(), "velocidade": 0.3},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo5/reflexo.png').convert_alpha(), "velocidade": 0.3},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo5/pedra-frente.png').convert_alpha(), "velocidade": 0.6}
            
            

        ]
        fundo_atual = []
        for camada in lista_de_camadas:
            imagem = camada["imagem"]
            velocidade = camada["velocidade"]
            imagem = pygame.transform.scale(imagem, (config.largura, config.altura))
            fundo_atual.append({
                "imagem": imagem,
                "velocidade": velocidade,
                "y": 0
            })

        cor_score =  (64,64,64)

    if fundoSorteado == 6:
        lista_de_camadas = [
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo6/ceu-mar.png').convert_alpha(), "velocidade": 0.05},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo6/estrelas.png').convert_alpha(), "velocidade": 0.02},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo6/nuvens-atras.png').convert_alpha(), "velocidade": 0.2},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo6/nuvens-frente.png').convert_alpha(), "velocidade": 0.5}
            
            

        ]
        fundo_atual = []
        for camada in lista_de_camadas:
            imagem = camada["imagem"]
            velocidade = camada["velocidade"]
            imagem = pygame.transform.scale(imagem, (config.largura, config.altura))
            fundo_atual.append({
                "imagem": imagem,
                "velocidade": velocidade,
                "y": 0
            })

        cor_score =  'white'

    if fundoSorteado == 7:
        lista_de_camadas = [
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo7/ceu-mar.png').convert_alpha(), "velocidade": 0.05},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo7/lua.png').convert_alpha(), "velocidade": 0.02},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo7/nuvens-atras.png').convert_alpha(), "velocidade": 0.15},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo7/nuvens.png').convert_alpha(), "velocidade": 0.10},
            {"imagem": pygame.image.load('graficos/fundo/FundosDivididos/fundo7/nuvens-baixo.png').convert_alpha(), "velocidade": 0.15}
        ]
        fundo_atual = []
        for camada in lista_de_camadas:
            imagem = camada["imagem"]
            velocidade = camada["velocidade"]
            imagem = pygame.transform.scale(imagem, (config.largura, config.altura))
            fundo_atual.append({
                "imagem": imagem,
                "velocidade": velocidade,
                "y": 0
            })

        cor_score =  'white'
    return fundo_atual, cor_score


def mostrar_fundo(fundo):
    config.screen.blit(fundo, (0, 0))

def mostrar_fundo_com_efeito(camada, velocidade, y, player_x):
    offset = (player_x * velocidade) % camada.get_width()
    config.screen.blit(camada, (-offset, y))
    config.screen.blit(camada, (-offset + camada.get_width(), y))







def barcoCheio(mensagem_text, mensagem_text_rect):
    if player.sprite.peso - player.sprite.pesoExtra >= 8:
        config.screen.blit(mensagem_text,mensagem_text_rect)


     