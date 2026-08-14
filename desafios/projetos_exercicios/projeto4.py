# Sistemas de fases.

jogador = {
    'nome': 'jj',
    'vida': 100,
    'ataque': 20,
    'nivel': 1,
    'experiencia': 0,
    'moedas': 20,
    'inventario': {
        'pocao': 2
    }
}

inimigo1 = {
    "nome": "Goblin",
    "vida": 40,
    "ataque": 10,
    "experiencia": 30,
    "moedas": 15
}

# Está dando erro por causa da função "ataque".
def ataque(atacante, vida):
    vida_atual = vida['vida'] - atacante['ataque']
    vida['vida'] = vida_atual

opcao_user = 0
print('\n----- Você encontrou um goblin -----')
print(f'\nSua vida: {jogador["vida"]}')
print(f'Vida do {inimigo1["nome"]}: {inimigo1["vida"]}')

while opcao_user != 3:

    print('\n1 - Atacar')
    print('2 - Usar poção')
    print('3 - Fugir')
    opcao_user = int(input('Escolha uma opção: '))

    if opcao_user == 1:
        print('\n------- Turno Jogador -------')
        print('Você atacou!')
        ataque(jogador['ataque'], inimigo1['vida'])
        print(f'Vida do inimigo: {inimigo1['vida']}')
        print('-'*25)
    elif opcao_user == 2:
        if jogador['vida'] < 100:
            print('-'*30)
            print('\nPoção de cura usada')
            jogador['inventario']['pocao'] -= 1
            print(f'Poções disponíveis: {jogador['inventario']['pocao']}')
        else:
            print('-'*30)
            print('Sua vida já está cheia!')

    if inimigo1['vida'] == 0:
        print(f'\nVocê derrotou {inimigo1["nome"]}\nVocê Venceu!🏆')
        break
    else:
        print(f'\nSua vida: {jogador["vida"]}')
        print(f'Vida do {inimigo1["nome"]}: {inimigo1["vida"]}')

    #turno inimigo
    if inimigo1['vida'] > 0:
        print('\n------- Turno Inimigo -------')
        print('Inimigo atacou!')
        ataque(inimigo1['ataque'], jogador['vida'])
        print(f'Sua vida: {jogador["vida"]}')
        print(f'Vida do {inimigo1["nome"]}: {inimigo1["vida"]}')
