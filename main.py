# Bibliotecas
import pygame, sys, os, random
from pygame.locals import *

# Alinhamento de tela # Centraliza a janela do jogo na tela
os.environ['SDL_VIDEO_CENTERED'] = '1'

def inicio1():
    # Inicializa o Pygame
    pygame.init()
    # Define o tamanho da tela
    tela = pygame.display.set_mode((850, 600))
    # Define o título da janela
    pygame.display.set_caption('Labirinto - Informática na Sociedade')

    # Cores usadas no jogo
    preto = (0, 0, 0)
    cor_titulo = (248, 248, 208)

    # Carrega imagens necessárias
    b1 = pygame.image.load('imagens/sistema/botaog.png')
    b2 = pygame.image.load('imagens/sistema/botaog.png')
    fundo = pygame.image.load('imagens/sistema/fundo.png')
    voltar = pygame.image.load('imagens/sistema/voltar.png')

    # Renderiza textos
    fonte1 = pygame.font.SysFont('Arial Black', 30)
    fonte2 = pygame.font.SysFont('Arial', 20)
    jogar = fonte1.render('Jogar', 1, cor_titulo)
    menu = fonte2.render('Menu Principal', 1, preto)

    # Loop principal do jogo
    while True:

        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    # Verifica se o botão "Voltar" foi clicado
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        print('Voltar selecionado')
                    # Verifica se o botão "Jogar" foi clicado
                    elif x > 500 and x < 750 and y > 330 and y < 430:
                        inicio2()
                    # Verifica se o botão "Menu Principal" foi clicado
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        print('Menu Principal selecionado')

        # Atualiza a tela com os objetos desenhados
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(b2, (500, 330))
        b2.blit(jogar, (25, 20))
        tela.blit(menu, (725, 570))
        pygame.display.update()


# Função para a tela de seleção de níveis
def inicio2():
    # Inicializa o Pygame
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Labirinto - Informática na Sociedade')

    # Cores
    preto = (0, 0, 0)
    cor_titulo = (248, 248, 208)

    # Carrega imagens necessárias
    b1 = pygame.image.load('imagens/sistema/botaop.png')
    b2 = pygame.image.load('imagens/sistema/botaop.png')
    fundo = pygame.image.load('imagens/sistema/fundo.png')
    voltar = pygame.image.load('imagens/sistema/voltar.png')

    # Renderiza textos
    fonte1 = pygame.font.SysFont('Arial Black', 45)
    fonte2 = pygame.font.SysFont('Arial', 20)
    facil = fonte1.render('Fácil', 1, cor_titulo)
    medio = fonte1.render('Médio', 1, cor_titulo)
    menu = fonte2.render('Menu Principal', 1, preto)

    # Loop principal do jogo
    while True:


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    # Verifica se o botão "Voltar" foi clicado
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        inicio1()
                    # Verifica qual nível foi selecionado
                    elif x > 150 and x < 350 and y > 305 and y < 385:
                        jogo('fácil')
                    elif x > 500 and x < 700 and y > 305 and y < 385:
                        jogo('médio')
                    # Verifica se o botão "Menu Principal" foi clicado
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        inicio1()

        # Atualiza
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(b1, (150, 305))
        b1.blit(facil, (36, 2))
        tela.blit(b2, (500, 305))
        b2.blit(medio, (25, 2))
        tela.blit(menu, (725, 570))
        pygame.display.update()


# Jogo
def jogo(nivel):
    # Inicialização do Pygame
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Labirinto - Informática na Sociedade')

    # Cores
    preto = (0, 0, 0)
    verde = (0, 255, 0)
    azul = (0, 78, 152)
    amarelo = (255, 238, 0)
    vermelho = (226, 0, 37)
    cor = preto

    # Carrega imagens
    fundo = pygame.image.load('imagens/sistema/fundo.png')
    voltar = pygame.image.load('imagens/sistema/voltar.png')
    labirinto = pygame.image.load('imagens/sistema/labirinto.png')

    # Renderiza
    fonte = pygame.font.SysFont('Arial', 20)
    menu = fonte.render('Menu Principal', 1, preto)

    # Lista de tuplas representando as posições das células no labirinto
    # Cada tupla contém as coordenadas (x, y) de uma célula
    posicoes = [(162, 195), (162, 375), (205, 375), (205, 335), (288, 335), (288, 376), (501, 376), (501, 336),
                (628, 336), (628, 376), (670, 376)]
    # Variáveis para acompanhar a posição atual do jogador no labirinto
    # Inicialmente definidas para a posição inicial (posicoes[0])
    posicao = 0  # Índice da posição atual na lista posicoes
    px = posicoes[0][0]  # Coordenada x da posição atual
    py = posicoes[0][1]  # Coordenada y da posição atual

    # Lista de movimentos que o jogador deve fazer para atravessar o labirinto.
    # Cada caractere representa uma direção (b - baixo, c - cima, d - direita).
    # Os movimentos são emparelhados com as posições no labirinto na ordem correta.
    movimentos = ['b', 'd', 'c', 'd', 'b', 'd', 'c', 'd', 'b', 'd']
    movimento = False

    # Declarações das perguntas e respostas
    if nivel == 'fácil':
        perguntas = {'1': [pygame.image.load('imagens/facil/p1.png'),
                           pygame.image.load('imagens/facil/a1.png'), pygame.K_b],
                     '2': [pygame.image.load('imagens/facil/p2.png'),
                           pygame.image.load('imagens/facil/a2.png'), pygame.K_c],
                     '3': [pygame.image.load('imagens/facil/p3.png'),
                           pygame.image.load('imagens/facil/a3.png'), pygame.K_c],
                     '4': [pygame.image.load('imagens/facil/p4.png'),
                           pygame.image.load('imagens/facil/a4.png'), pygame.K_a],
                     '5': [pygame.image.load('imagens/facil/p5.png'),
                           pygame.image.load('imagens/facil/a5.png'), pygame.K_d],
                     '6': [pygame.image.load('imagens/facil/p6.png'),
                           pygame.image.load('imagens/facil/a6.png'), pygame.K_a],
                     '7': [pygame.image.load('imagens/facil/p7.png'),
                           pygame.image.load('imagens/facil/a7.png'), pygame.K_c],
                     '8': [pygame.image.load('imagens/facil/p8.png'),
                           pygame.image.load('imagens/facil/a8.png'), pygame.K_d],
                     '9': [pygame.image.load('imagens/facil/p9.png'),
                           pygame.image.load('imagens/facil/a9.png'), pygame.K_c],
                     '10': [pygame.image.load('imagens/facil/p10.png'),
                            pygame.image.load('imagens/facil/a10.png'), pygame.K_c]}
    elif nivel == 'médio':
        perguntas = {'1': [pygame.image.load('imagens/medio/p1.png'),
                           pygame.image.load('imagens/medio/a1.png'), pygame.K_c],
                     '2': [pygame.image.load('imagens/medio/p2.png'),
                           pygame.image.load('imagens/medio/a2.png'), pygame.K_c],
                     '3': [pygame.image.load('imagens/medio/p3.png'),
                           pygame.image.load('imagens/medio/a3.png'), pygame.K_a],
                     '4': [pygame.image.load('imagens/medio/p4.png'),
                           pygame.image.load('imagens/medio/a4.png'), pygame.K_b],
                     '5': [pygame.image.load('imagens/medio/p5.png'),
                           pygame.image.load('imagens/medio/a5.png'), pygame.K_b],
                     '6': [pygame.image.load('imagens/medio/p6.png'),
                           pygame.image.load('imagens/medio/a6.png'), pygame.K_a],
                     '7': [pygame.image.load('imagens/medio/p7.png'),
                           pygame.image.load('imagens/medio/a7.png'), pygame.K_a],
                     '8': [pygame.image.load('imagens/medio/p8.png'),
                           pygame.image.load('imagens/medio/a8.png'), pygame.K_b],
                     '9': [pygame.image.load('imagens/medio/p9.png'),
                           pygame.image.load('imagens/medio/a9.png'), pygame.K_a],
                     '10': [pygame.image.load('imagens/medio/p10.png'),
                            pygame.image.load('imagens/medio/a10.png'), pygame.K_c]}
    # Sorteio de uma pergunta aleatória para o jogo.
    sorteio = random.randint(1, len(perguntas))
    sorteados = []
    sorteados.append(sorteio)
    # Variáveis de controle para as opções de cores e respostas corretas/incorretas.
    colorm = colort = correto = incorreto = False

    # Loop
    while True:

        # Captura os eventos do pygame
        for event in pygame.event.get():
            # Verifica se o evento é de saída do jogo
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Verifica se o mouse está em movimento
            if event.type == pygame.MOUSEMOTION:
                # Captura a posição do mouse
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # Verifica se o mouse está sobre uma das opções de resposta e se não foi selecionada nenhuma opção
                if x > 48 and x < 802 and y > 435 and y < 463 and colort == False:
                    colorm = True
                    evento = 'a'
                elif x > 48 and x < 802 and y > 464 and y < 492 and colort == False:
                    colorm = True
                    evento = 'b'
                elif x > 48 and x < 802 and y > 493 and y < 521 and colort == False:
                    colorm = True
                    evento = 'c'
                elif x > 48 and x < 802 and y > 522 and y < 550 and colort == False:
                    colorm = True
                    evento = 'd'
                else:
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    colorm = False
            # Verifica se houve clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    # Verifica se o botão de voltar foi pressionado
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        inicio2()
                    # Verifica se o botão de reiniciar foi pressionado
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        inicio1()
                    # Verifica se uma das opções de resposta foi selecionada
                    elif x > 48 and x < 802 and y > 435 and y < 463:
                        colort = True
                        evento = 'a'
                        # Verifica se a resposta selecionada está correta
                        if perguntas[str(sorteio)][2] == pygame.K_a:
                            correto = True
                        else:
                            incorreto = True
                    elif x > 48 and x < 802 and y > 464 and y < 492:
                        colort = True
                        evento = 'b'
                        if perguntas[str(sorteio)][2] == pygame.K_b:
                            correto = True
                        else:
                            incorreto = True
                    elif x > 48 and x < 802 and y > 493 and y < 521:
                        colort = True
                        evento = 'c'
                        if perguntas[str(sorteio)][2] == pygame.K_c:
                            correto = True
                        else:
                            incorreto = True
                    elif x > 48 and x < 802 and y > 522 and y < 550:
                        colort = True
                        evento = 'd'
                        if perguntas[str(sorteio)][2] == pygame.K_d:
                            correto = True
                        else:
                            incorreto = True
            # Verifica se uma tecla foi pressionada
            if event.type == pygame.KEYDOWN:
                # Verifica se o jogador ainda não chegou ao final do labirinto
                if posicao != len(posicoes) - 1:
                    # Verifica qual tecla foi pressionada e se corresponde à resposta correta
                    if event.key == K_a:
                        colort = True
                        evento = 'a'
                        if perguntas[str(sorteio)][2] == pygame.K_a:
                            correto = True
                        else:
                            incorreto = True
                    elif event.key == K_b:
                        colort = True
                        evento = 'b'
                        if perguntas[str(sorteio)][2] == pygame.K_b:
                            correto = True
                        else:
                            incorreto = True
                    elif event.key == K_c:
                        colort = True
                        evento = 'c'
                        if perguntas[str(sorteio)][2] == pygame.K_c:
                            correto = True
                        else:
                            incorreto = True
                    elif event.key == K_d:
                        colort = True
                        evento = 'd'
                        if perguntas[str(sorteio)][2] == pygame.K_d:
                            correto = True
                        else:
                            incorreto = True
                    else:
                        fim1()
            # Verifica se a resposta foi correta
            if correto == True:
                # Define a cor verde para indicar a resposta correta
                cor = verde
                # Atualiza a posição do jogador no labirinto
                if movimentos[posicao] == 'b':
                    a = py
                    b = posicoes[posicao + 1][1]
                    tipo = 'b'
                elif movimentos[posicao] == 'c':
                    b = py
                    a = posicoes[posicao + 1][1]
                    tipo = 'c'
                elif movimentos[posicao] == 'd':
                    a = px
                    b = posicoes[posicao + 1][0]
                    tipo = 'd'
                elif movimentos[posicao] == 'e':
                    b = px
                    a = posicoes[posicao + 1][0]
                    tipo = 'e'
                # Define que houve movimento
                movimento = True
                # Atualiza a posição atual do jogador
                posicao += 1
                # Bloqueia eventos de tecla e mouse para evitar movimentos incorretos
                pygame.event.set_blocked(pygame.KEYDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                # Reinicia a variável de controle de correto
                correto = False
            # Verifica se a resposta foi incorreta
            if incorreto == True:
                # Verifica se o jogador não está na posição inicial
                if posicao != 0:
                    # Define a cor vermelha para indicar a resposta incorreta
                    cor = vermelho
                    # Atualiza a posição do jogador para a anterior
                    if movimentos[posicao - 1] == 'b':
                        b = py
                        a = posicoes[posicao - 1][1]
                        tipo = 'c'
                    elif movimentos[posicao - 1] == 'c':
                        a = py
                        b = posicoes[posicao - 1][1]
                        tipo = 'b'
                    elif movimentos[posicao - 1] == 'd':
                        b = px
                        a = posicoes[posicao - 1][0]
                        tipo = 'e'
                    elif movimentos[posicao - 1] == 'e':
                        a = px
                        b = posicoes[posicao - 1][0]
                        tipo = 'e'
                    # Define que houve movimento
                    movimento = True
                    # Atualiza a posição atual do jogador para a anterior
                    posicao -= 1
                    # Bloqueia eventos de tecla e mouse para evitar movimentos incorretos
                    pygame.event.set_blocked(pygame.KEYDOWN)
                    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                else:  # Caso o jogador esteja na posição inicial, sorteia uma nova pergunta
                    sorteio = random.randint(1, len(perguntas))
                    # Verifica se a pergunta sorteada já foi utilizada
                    while sorteio in sorteados:
                        # Se todas as perguntas já foram sorteadas, reinicia a lista de perguntas sorteadas
                        if len(sorteados) == len(perguntas):
                            sorteados = []
                        # Sorteia uma nova pergunta
                        sorteio = random.randint(1, len(perguntas))
                    # Adiciona a pergunta sorteada à lista de perguntas sorteadas
                    sorteados.append(sorteio)
                    # Apaga o retângulo atual representando a posição do jogador
                    pygame.draw.rect(tela, vermelho, (px, py, 20, 20))
                    pygame.display.update()
                    # Aguarda
                    pygame.time.delay(500)
                # Reinicia a variável de controle de incorreto
                incorreto = False

        # Objetos e tela
        # Limpa a tela desenhando o fundo
        tela.blit(fundo, (0, 0))
        # Desenha o botão "Voltar"
        tela.blit(voltar, (10, 10))
        # Desenha o botão "Menu"
        tela.blit(menu, (725, 570))
        # Desenha a pergunta atual na tela
        tela.blit(perguntas[str(sorteio)][0], (40, 40))
        # Desenha o labirinto na tela
        tela.blit(labirinto, (40, 185))
        # Desenha as opções de resposta na tela
        tela.blit(perguntas[str(sorteio)][1], (40, 425))
        # Desenha o jogador na posição atual com a cor definida
        pygame.draw.rect(tela, cor, (px, py, 20, 20))
        # Verifica se há movimento do jogador
        if movimento == True:
            # Move o jogador na direção especificada até alcançar a próxima posição no labirinto
            if tipo == 'b':
                # Move o jogador para baixo
                if a + 5 > b:
                    py += 1
                    a = py
                else:
                    py += 5
                    a = py
            elif tipo == 'c':
                # Move o jogador para cima
                if a + 5 > b:
                    py -= 1
                    b = py
                else:
                    py -= 5
                    b = py
            elif tipo == 'd':
                # Move o jogador para a direita
                if a + 5 > b:
                    px += 1
                    a = px
                else:
                    px += 5
                    a = px
            elif tipo == 'e':
                # Move o jogador para a esquerda
                if a + 5 > b:
                    px -= 1
                    b = px
                else:
                    px -= 5
                    b = px
            # Verifica se o jogador alcançou a próxima posição no labirinto
            if a == b:
                # Define a cor do jogador como preto
                cor = preto
                # Define que não há mais movimento
                movimento = False
                # Define que o jogador não está sobre uma resposta
                colort = False
                colotm = True
                # Define que o jogo pode aceitar apenas eventos de mouse
                pygame.event.set_allowed(None)
                # Verifica se o jogador alcançou a posição final do labirinto
                if posicao == len(posicoes) - 1:
                    i = 0
                    # Animação de vitória
                    pygame.display.update()
                    while i < 50:
                        pygame.time.delay(300)
                        pygame.draw.rect(tela, preto, (px, py, 20, 20))
                        pygame.display.update()
                        pygame.time.delay(300)
                        pygame.draw.rect(tela, verde, (px, py, 20, 20))
                        pygame.display.update()
                        i += 10
                    # Chama a função de fim de jogo
                    fim1()
                # Sorteia uma nova pergunta
                sorteio = random.randint(1, len(perguntas))
                # Verifica se a pergunta sorteada já foi utilizada
                while sorteio in sorteados:
                    if len(sorteados) == len(perguntas):
                        sorteados = []
                    sorteio = random.randint(1, len(perguntas))
                # Adiciona a pergunta sorteada à lista de perguntas sorteadas
                sorteados.append(sorteio)
        # Desenha um círculo indicando a opção selecionada pelo jogador
        if colorm == True:
            if evento == 'a':
                pygame.draw.circle(tela, azul, (67, 447), 13)
            elif evento == 'b':
                pygame.draw.circle(tela, amarelo, (67, 477), 13)
            elif evento == 'c':
                pygame.draw.circle(tela, vermelho, (67, 507), 13)
            elif evento == 'd':
                pygame.draw.circle(tela, verde, (67, 537), 13)
            # Verifica se há movimento e se o jogador selecionou uma resposta
            if movimento == True and colort == True:
                colorm = False
        # Desenha um círculo indicando a opção selecionada pelo jogador
        if colort == True:
            if evento == 'a':
                pygame.draw.circle(tela, azul, (67, 447), 13)
            elif evento == 'b':
                pygame.draw.circle(tela, amarelo, (67, 477), 13)
            elif evento == 'c':
                pygame.draw.circle(tela, vermelho, (67, 507), 13)
            elif evento == 'd':
                pygame.draw.circle(tela, verde, (67, 537), 13)
            # Verifica se o jogador está na posição inicial e se não há movimento
            if posicao == 0 and movimento == False:
                colort = False
        pygame.display.update()  # Atualiza a tela


def fim1():
    # Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('Labirinto - Informática na Sociedade')

    # Cores
    preto = (0, 0, 0)

    # Caarega Imagens
    parabens = pygame.image.load('imagens/sistema/parabens.png')
    fim = pygame.image.load('imagens/sistema/fim.png')
    fundo = pygame.image.load('imagens/sistema/fundo.png')
    voltar = pygame.image.load('imagens/sistema/voltar.png')

    # Textos
    fonte1 = pygame.font.SysFont('Arial Black', 25)
    fonte2 = pygame.font.SysFont('Arial', 20)
    menu = fonte2.render('Menu Principal', 1, preto)

    # Loop
    while True:

        # Tratamento dos eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    # Verifica se o usuário clicou no botão "Voltar"
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        inicio2()
                    # Verifica se o usuário clicou no botão "Menu Principal"
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        inicio1()

        # Objetos e tela
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(parabens, (217, 60))
        tela.blit(fim, (40, 180))
        pygame.draw.rect(tela, preto, (275, 485, 300, 5))
        tela.blit(menu, (725, 570))
        pygame.display.update()



inicio1()
