# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Imports
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

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
     def __init__(self, palavra):
          self.palavra = palavra
          self.letras_erradas = []
          self.letras_escolhidas = []

	# Método para adivinhar a letra
     def guess(self, letra):
         
         if letra in self.palavra and letra not in self.letras_escolhidas:
             self.letras_escolhidas.append(letra)
          
         elif letra not in self.palavra and letra not in self.letras_erradas:
             self.letras_erradas.append(letra)
	
         else:
             return False
         
         return False
     
	# Método para verificar se o jogo terminou
     def hangman_over(self):
         
         return self.hangman_won() or (len(self.letras_erradas) == 6)
     	
	# Método para verificar se o jogador venceu
     def hangman_won(self):
         
         if '_' not in self.hide_palavra():
             return True
         return False
     
	# Método para não mostrar a letra no board
     def hide_palavra(self):
         
         rtn = ''

         for letra in self.palavra:
             if letra not in self.letras_escolhidas:
                 rtn += '_'
             else:
                 rtn += letra
         return rtn
     
	# Método para checar o status do game e imprimir o board na tela
     def print_game_status(self):
         
         print(board[len(self.letras_erradas)])

         print('\nPalavra: ' + self.hide_palavra())

         print('\nLetras erradas: ',)

         for letra in self.letras_erradas:
             print(letra,)

         print()

         print('Letras corretas: ',)

         for letra in self.letras_escolhidas:
             print(letra,)
          
         print()

# Método para ler uma palavra de forma aleatórioa do banco de palavras
def rand_palavra():
    
     palavras = ['abacaxi', 'laranja', 'kiwi', 'caju', 'goiaba', 'manga', 'morango', 'cereja', 'pitaya', 'jabuticaba']

     palavra = random.choice(palavras)

     return palavra

# Método Main
def main():
    
    limpa_tela()

    # Cria o objeto e seleciona uma palavra randomicamente
    game = Hangman(rand_palavra())

    # Enquanto jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        
        # Status do game
        game.print_game_status()

        # Recebe input do terminal
        user_input = input('\nDigite uma letra: ')

        # Verifica se a letra digitada faz parte da palavra
        game.guess(user_input)

    # Verifica status do jogo
    game.print_game_status()

    # Conforme o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')

    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

# Executa o programa
if __name__ == "__main__":
    main()