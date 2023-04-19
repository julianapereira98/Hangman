# Projeto 1 - Desenvolvimento de Game em Linguagem Python - V1

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

def game():

    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Advinhe a palavra abaixo:\n')

    # Lista de palavras para o jogo
    palavras = ['abacaxi', 'laranja', 'kiwi', 'caju', 'goiaba', 'manga', 'morango', 'cereja', 'pitaya', 'jabuticaba']

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 7

    letras_erradas = []

    while chances > 0:

        print(' '.join(letras_descobertas))
        print('\nChaces restantes: ', chances)
        print('Letras erradas:', ' '.join(letras_erradas))

        tentativa = input('\nDigite uma letra: ').lower()

        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1

            letras_erradas.append(tentativa)

        if '_' not in letras_descobertas:
            print('\nVocê venceu, a palavra era:', palavra)
            break
        
    if '_' in letras_descobertas:
        print('\nVocê perdeu, a palavra era:', palavra)

if __name__ == "__main__":
    game()


        

    
    