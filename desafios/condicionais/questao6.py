# Verificação de estoque 

stock_dispo = input('\nQual a quantidade de estoque disponível? ')
stock_pedi = input('Quantidade pedida: ')

if stock_pedi > stock_dispo:
    print('Estoque insuficiente\n')
else:
    print('Pedido confirmado\n')
