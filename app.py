from desenho import desenhar_forca
from dataset import *
import random

# inicio do programa
print("\nBem vindo ao jogo da forca!\n")
print("Adivinhe a palavra abaixo: \n")

# definindo os erros e chamando o desenho base da forca
erros = 0
desenhar_forca(erros)

# chamando uma palavra aleatória dos datasets salvos
palavraRodada = random.choice(frutas)
palavra = []

# cria as barras das letras necessárias para formar a palavra
for i in range(len(palavraRodada)):
    palavra.append("__")

# lista de letras que foram jogadas
letras = []

while(erros<=7):
    print("\nPalavra: ", palavra, "\n")
    letraRodada = input("\nDigite uma letra: ")

    # verifica se a letra já foi jogada
    if letraRodada in letras:
        print("Você já tentou essa letra. Escolha outra!")
    # se não realiza o jogo
    else:
        letras.append(letraRodada)
        # verifica se a letra jogada não está na palavra 
        if letraRodada not in palavraRodada:
            print("Ops, esta letra não está na palavra!")
            print("Tentativas restantes: ", 7 - erros)
            erros += 1
            desenhar_forca(erros)
        else:
            # percorre toda a palavra comparando a letra jogada com as letras da palavra
            for i in range(len(palavraRodada)):
                if letraRodada == palavraRodada[i]:
                    palavra[i] = letraRodada

            print("Você acertou a letra!")
            desenhar_forca(erros)
            print("\nPalavra: ", palavra, "\n")
    
    # se esgotar as chances de erro (7) você perde e o jogo para
    if erros == 7:
        print("Você perdeu! A palavra era: ", palavraRodada)
        break

    # verificar se todos os itens de palavra sejam caracteres do alfabeto e não apenas strings
    if all(item.isalpha() for item in palavra):
        print("Parabéns! Você acertou a palavra!")
        break
