from time import sleep
from random import randint

from utils.fonte_cor import adiciona_cor


def cria_tabuleiro(jogador):
    tabuleiro = {
        'jogador': jogador,
        'area': []
    }
    for i in range(0, 10):
        linha = []
        for j in range(0, 10):
            linha.append(None)
        tabuleiro['area'].append(linha)

    return tabuleiro


def mensagem_criacao_jogador(jogador):
    print(f'Criação do jogador {jogador}')


def mensagem_inicializacao():
    print('==== Iniciando Jogo =====')
    print('==== Batalha Naval =====')


def mostrar_tabuleiro(tabuleiros):
    for i, tabuleiro in enumerate(tabuleiros):
        id_jogador = tabuleiro['jogador']['id']
        area = tabuleiro['area']
        for j, linha in enumerate(area):
            if j == 0 and id_jogador == 1:
                mostrar_indice_coluna(len(linha))
            mostrar_indice_linha(j)
            for posicao in linha:
                cor = '31m' if id_jogador == 1 else '34m'
                print(f'{adiciona_cor(cor, " * ")}', end=' ')
            print()
            if j == len(area) - 1 and id_jogador == 2:
                mostrar_indice_coluna(len(linha))
            sleep(0.05)
        if i == 0:
            print(' = ' * 13)


def mostrar_indice_coluna(tamanho_linha):
    for count in range(0, tamanho_linha):
        end = '\n' if count == tamanho_linha - 1 else ' '
        espaco_extra = '  ' if count == 0 else ''
        print(f'{espaco_extra} {adiciona_cor("33m", count)} ', end=end)


def mostrar_indice_linha(indice):
    print(adiciona_cor("33m", indice), end=':')


def pedir_nome():
    return input('Informe o seu nome: ')


def criar_jogadores():
    mensagem_criacao_jogador('Jogador 1')
    jogador1 = criar_jogador(1)
    mensagem_criacao_jogador('Jogador 2')
    jogador2 = criar_jogador(2)
    return jogador1, jogador2


def criar_jogador(id):
    nome = pedir_nome()
    return {
        'id': id,
        'nome': nome,
        'pontos': 0,
        'vez': False
    }


def sortear_jogador_inicial(jogador1, jogador2):
    jogadores = jogador1, jogador2
    numero_sorteado = randint(0, 1)
    jogadores[numero_sorteado]['vez'] = True
    return jogadores


def placar(jogador1, jogador2):
    print('==== Placar ====')
    nomej1, pontosj1, nomej2, pontosj2 = jogador1.get('nome'), jogador1.get('pontos'), \
                                         jogador2.get('nome'), jogador2.get('pontos')
    print(f'{nomej1} está com {pontosj1} pontos e {nomej2} está com {pontosj2} pontos')
    nome_jogador_da_vez = jogador1.get('nome') if jogador1.get('vez') else jogador2.get('nome')
    print(f'A vez de jogar é de {nome_jogador_da_vez}')


def posiciona_barco():
    tabuleiro =  

def rodar_programa():
    mensagem_inicializacao()
    jogador1, jogador2 = criar_jogadores()
    jogador1, jogador2 = sortear_jogador_inicial(jogador1, jogador2)
    placar(jogador1, jogador2)
    tabuleiros = cria_tabuleiro(jogador1), cria_tabuleiro(jogador2)
    mostrar_tabuleiro(tabuleiros)
    # Posicionamento dos barcos
    # Batalha, ou seja, jogadores atirando um no outro até que um seja derrotado!
    # mostra o vencedor


rodar_programa()

