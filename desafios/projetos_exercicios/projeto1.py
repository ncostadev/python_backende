# Sistema de batalha
jogador = {
    'nome': '',
    'vida': 1000,
    'ataque': 25,
    'defesa': 10,
    'ataque_critico': 35 
}

inimigo = {
    'nome': 'Slime',
    'vida': 800,
    'ataque': 25,
    'defesa': 10,
    'ataque_critico': 28 
}

def calcular_dano(ataque, defesa):
    dano = ataque - defesa
    if dano <= 0:
        dano = 0
    return dano
    

def atacar(atacante, defensor):
    dano = calcular_dano(atacante['ataque'], defensor['defesa'])
    defensor['vida'] -= dano
    if defensor['vida'] <=0: 
        defensor['vida'] = 0

    print(f'{atacante['nome']} atacou')
    print(f'{defensor['nome']} causando {dano} de dano')
    print(f'Vida de {defensor['nome']}: {defensor['vida']}')

def ataque_critico(atacante, defensor):
    dano = calcular_dano(atacante['ataque_critico'], defensor['defesa'])
    defensor['vida'] -= dano
    if defensor['vida'] <= 0:
        defensor['vida'] = 0
    print(f'{atacante['nome']} Deu Dano crítico! 🗡️')
    print(f'Vida de {defensor['nome']}: {defensor['defesa']}')

def nome_jogador(nome):
    jogador['nome'] = nome



player1 = input('Qual seu nome? ')
nome_jogador(player1)
        

print('===== ⚔️ Batalha ⚔️ =====')

while jogador['vida'] > 0 and inimigo['vida'] > 0:
    print('\n---Turno do jogador---')
    atacar(jogador, inimigo)

    if inimigo['vida'] <= 0:
        print('\n🏆 Você venceu!!')
        break
    print('\n---Turno do Inimigo---')
    atacar(inimigo, jogador)

    if jogador['vida'] <= 0:
        print('\n 🦠Você perdeu!!')
        break

