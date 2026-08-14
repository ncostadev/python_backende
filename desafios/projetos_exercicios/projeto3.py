# Loja de RPG


produtos = {
    'pocao de cura': {
        'preco': 25.90,
        'estoque': 10
    },
    'espada de ferro': {
        'preco': 15.00,
        'estoque': 8
    },
    'manto de protecao': {
        'preco': 35.00,
        'estoque': 6
    },
    'rolo de magia': {
        'preco': 20.00,
        'estoque': 2
    },
    'cajado': {
        'preco': 30.00,
        'estoque': 3
    }

}

saldo = 100

def comprar(produto):
    global saldo
    if saldo <= 0 and produto == 1:
        print('Saldo insufuciente!')
        print(f'Saldo atual: R${saldo}')
    elif produto == 1 and produtos['pocao de cura']['estoque'] > 0:
        saldo -= produtos['pocao de cura']['preco']
        print(f'Saldo atual: R${saldo}')
    elif produtos['pocao de cura']['estoque'] <= 0 and produto == 1:
        print('Sem estoque')
    
    if saldo <= 0 and produto == 2:
        print('Saldo insufuciente!')
        print(f'Saldo atual: R${saldo}')
    elif produto == 2 and produtos['espada de ferro']['estoque'] > 0:
        saldo -= produtos['espada de ferro']['preco']
        print(f'Saldo atual: R${saldo}')
    elif produtos['espada de ferro']['estoque'] <= 0 and produto == 2:
        print('Sem estoque')

    if saldo <= 0 and produto == 3:
        print('Saldo insufuciente!')
        print(f'Saldo atual: R${saldo}')
    elif produto == 3 and produtos['manto de protecao']['estoque'] > 0:
        saldo -= produtos['manto de protecao']['preco']
        print(f'Saldo atual: R${saldo}')
    elif produtos['manto de protecao']['estoque'] <= 0 and produto == 3:
        print('Sem estoque')

    if saldo <= 0 and produto == 4:
        print('Saldo insufuciente!')
        print(f'Saldo atual: R${saldo}')
    elif produto == 4 and produtos['rolo de magia']['estoque'] > 0:
        saldo -= produtos['rolo de magia']['preco']
        print(f'Saldo atual: R${saldo}')
    elif produtos['rolo de magia']['estoque'] <= 0 and produto == 4:
        print('Sem estoque')

    if saldo <= 0 and produto == 5:
        print('Saldo insufuciente!')
        print(f'Saldo atual: R${saldo}')
    elif produto == 5 and produtos['cajado']['estoque'] > 0:
        saldo -= produtos['cajado']['preco']
        print(f'Saldo atual: R${saldo}')
    elif produtos['cajado']['estoque'] <= 0 and produto == 5:
        print('Sem estoque')
    
opcao_user = 0

# saldo_user = int(input('Qual seu saldo: '))

while opcao_user != 3: 
    print('\n----- LOJA -----')
    print('''1 - Ver Produtos
2 - Verificar Saldo
3 - Sair''')
    opcao_user = int(input('Escolha uma opção: '))

    if opcao_user == 1:
        print('\n----- PRODUTOS -----')
        print('1 - Poção De Cura')
        print('2 - Espada De Ferro')
        print('3 - Manto De Proteção')
        print('4 - Rolo De Magia')
        print('5 - Cajado')
        opcao_produto = int(input('\nEscolha uma opção: '))

        # Sistema para visualizar o produto
        if opcao_produto == 1:
            print('\n')
            print('-'*35)
            print('-- POÇÃO DE CURA --')
            print(
                f'Preço: R${produtos['pocao de cura']['preco']}\nSeu Saldo: R${saldo}')
            compra = (input('Deseja Comprar? ')).lower()
            print('-'*35)
            if compra == 'sim':
                comprar(1)

        if opcao_produto == 2:
            print('\n')
            print('-'*35)
            print('-- ESPADA DE FERRO --')
            print(
                f'Preço: R${produtos['espada de ferro']['preco']}\nSeu Saldo: R${saldo}')
            compra = (input('Deseja Comprar? ')).lower()
            print('-'*35)
            if compra == 'sim':
                comprar(2)

        if opcao_produto == 3:
            print('\n')
            print('-'*35)
            print('-- MANTO DE PROTEÇÃO --')
            print(
                f'Preço: R${produtos['manto de protecao']['preco']}\nSeu Saldo: R${saldo}')
            compra = (input('Deseja Comprar? ')).lower()
            print('-'*35)
            if compra == 'sim':
                comprar(3)

        if opcao_produto == 4:
            print('\n')
            print('-'*35)
            print('-- ROLO DE MAGIA --')
            print(f'Preço: R${produtos['rolo de magia']['preco']}\nSeu Saldo: R${saldo}')
            compra = (input('Deseja Comprar? ')).lower()
            print('-'*35)
            if compra == 'sim':
                comprar(4)

        if opcao_produto == 5:
            print('\n')
            print('-'*35)
            print('-- CAJADO --')
            print(f'Preço: R${produtos['cajado']['preco']}\nSeu Saldo: R${saldo}')
            compra = (input('Deseja Comprar? ')).lower()
            print('-'*35)
            if compra == 'sim':
                comprar(5)

    if opcao_user == 2:
        print(f'Seu saldo: R${saldo}')
        de = input('Quer depositar? ').lower()
        if de == 'sim':
            valor = int(input('Quanto você quer depositar? R$: '))
            saldo += valor
            print(f'Seu saldo: R${saldo}')
