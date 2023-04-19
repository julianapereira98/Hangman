# Projeto 1 - Desenvolvimento de Game em Linguagem Python - V2

import random
from os import system, name

def limpa_tela():
    """
    Função para limpar tela a cada execução
    """

    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

def display_hangman(chances):
    """
    Função que desenha a forca na tela 
    """

    stages = [
        """
            ---------
            |       | 
            |       O
            |      \\|/
            |       |
            |      / \\
            _
        """,
        """
            ---------
            |       | 
            |       O
            |      \\|/
            |       |
            |      / 
            _
        """,
        """
            ---------
            |       | 
            |       O
            |      \\|/
            |       |
            |
            _
        """,
        """
            ---------
            |       | 
            |       O
            |      \\|
            |       |
            |
            _
        """,
        """
            ---------
            |       | 
            |       O
            |       |
            |       |
            |
            _
        """,
        """
            ---------
            |       | 
            |       O
            |
            |
            |
            _
        """,
        """
            ---------
            |       | 
            |
            |
            |
            |
            _
        """
    ]
    return stages[chances]

def game():

    """
    Função que executa o jogo.
    """

    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Advinhe a palavra abaixo:\n')

    # Lista de palavras para o jogo
    palavras = ['abacaxi', 'laranja', 'kiwi', 'caju', 'goiaba', 'manga', 'morango', 'cereja', 'pitaya', 'jabuticaba']

    palavra = random.choice(palavras)

    lista_letras_palavras = [letra for letra in palavra]

    tabuleiro = ['_'] * len(palavra)

    chances = 6

    letras_tentativas = []

    while chances > 0:

        print(display_hangman(chances))
        print('Palavra:', tabuleiro)
        print('\n')

        tentativa = input('Digite uma letra: ').lower()

        if tentativa in letras_tentativas:
            print('Você já tentou essa letra. Escolha outra!')
            continue

        letras_tentativas.append(tentativa)

        if tentativa in lista_letras_palavras:

            print('Você acertou a letra!')

            for i in range(len(lista_letras_palavras)):
                if lista_letras_palavras[i] == tentativa:
                    tabuleiro[i] = tentativa
            
            if '_' not in tabuleiro:
                print('\nVocê venceu! A palavra era: {}'.format(palavra))
                break
        else:
            print('Ops. Essa letra não está na palavra!')
            chances -= 1

    if '_' in tabuleiro:
            print('\nVocê perdeu! A palavra era: {}.'.format(palavra))


if __name__ == "__main__":
    game()
