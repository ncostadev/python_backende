# O jogo de adivinhação

import random

numero_aleatorio = random.randint(1, 100)

# Quantidade de tentativas.
tentativas = 7

# Sistema de pontuação.
pontuacao = 0
tentativas_atual = 0



print(numero_aleatorio)
print('\n----- ADIVINHE O NÚMERO -----')
while tentativas > 0:
    numero_usuario = int(input('\nDe 1 a 100: '))
    tentativas -= 1
    tentativas_atual += 1
    
    # Sistema de pontuação
    if tentativas_atual == 1:
        pontuacao = 100
    elif tentativas_atual == 2:
        pontuacao = 80
    elif tentativas_atual == 3:
        pontuacao = 60


    if numero_usuario == numero_aleatorio:
        print('-'*20)
        print('\n----- VITÓRIA!!🏆 -----')
        print(f'Resposta: {numero_aleatorio}')
        print('-'*20)


        print(pontuacao)
        break

    if tentativas == 1:
        print('-'*20)
        print(f'Errou! Tente De novo\nVocê tem mais {tentativas} Tentativa!')
    elif numero_usuario != numero_aleatorio and tentativas != 0 and tentativas != 1:
        print('-'*20)
        print(f'Errou! Tente De novo\nVocê tem mais {tentativas} Tentativas!')
    else:
        print('Errou!')
        

    if numero_usuario < numero_aleatorio and tentativas != 0:
        print('O número é MAIOR')
    elif numero_usuario > numero_aleatorio and tentativas != 0:
        print('O número é MENOR')
    print('-'*20)




if numero_usuario != numero_aleatorio:
    print('\n-----❌ PERDEU ❌-----')
    print('Fim de jogo!')
    print(f'Resposta: {numero_aleatorio}')

