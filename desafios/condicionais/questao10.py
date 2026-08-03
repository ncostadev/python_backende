# Crie um menu de escolha utilizando número a escolha tem de ser 1 a 5 e no final deve mostrar o número escolhido.

menu = '''
1 - Banana
2 - Maçã
3 - Kiwi
4 - Uva
5 - Laranja
'''
print(menu)
escolha = int(input('Escolha uma opção digitando o número: '))

if escolha == 1:
    print('\nBanana')
elif escolha == 2:
    print('\nMaçã')
elif escolha == 3:
    print('\nkiwi')
elif escolha == 4:
    print('\nUva')
elif escolha == 5:
    print('\nLaranja')

